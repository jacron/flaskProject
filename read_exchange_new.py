from lib.exchange import get_version, get_exchange_def, get_field_def, \
    get_record_def_by_code, names


def get_f_def(field_defs_, name):
    for field_def in field_defs_['fields']['field']:
        if field_def['name'] == name:
            return field_def
    return None


def get_field(rec, field_defs_, line):
    try:
        begin = int(rec['@pos']) - 1
        field_def = get_f_def(field_defs_, rec['@name'])
        field_length = int(field_def['length'])
        end = begin + field_length
        if begin + 1 > len(line):
            lin = ''
        else:
            lin = line[begin:end]
        input_type = 'text'
        if field_def['typedef'] == 'num':
            input_type = 'number'
        alignment_ = 'right'
        if field_def.get('alignment') == 'left':
            alignment_ = 'left'
        return {
            'value': lin.strip(),
            'length': field_length,
            'type': input_type,
            'alignment': alignment_
        }
    except Exception as e:
        print(e)
        print(rec)
        print(f'length of line={len(line)}')
        return None


def parse_line(line, record_def, field_defs_):
    record = dict()
    for rec in record_def:
        field = get_field(rec, field_defs_, line)
        if field:
            record[rec['@name']] = field
    record['name'] = names[record['type']['value']]
    return record


def get_record_type_def(line, def_):
    code_ = line[:2]
    record_def = get_record_def_by_code(code_, def_)
    return record_def


def get_records(lines, version):
    def_ = get_exchange_def(version)
    field_defs_ = get_field_def(version)
    records = []
    meta = dict()
    for line in lines:
        if line.startswith('#'):
            parts = line[2:].split(': ')
            prefix = parts[0][1:]
            value = parts[1]
            meta[prefix] = value
        else:
            record_def = get_record_type_def(line, def_)
            record = parse_line(line.strip(), record_def, field_defs_)
            if record:
                records.append(record)
    return records, meta


def read_exchange_new(filename, dir_):
    with open(dir_ + filename) as fp:
        lines = fp.readlines()
    version = get_version(lines)
    data = dict()
    data['lines'] = lines
    data['records'], data['meta'] = get_records(lines, version)
    data['version'] = version
    return data
