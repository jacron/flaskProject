
from lib.exchange import get_version, get_exchange_def, get_field_def, \
    get_record_def_by_code


def add_meta(line, data):
    prefix = '$Vn: '
    if line.startswith(prefix):
        data['Version'] = line[len(prefix):]
    prefix = '$NR: '
    if line.startswith(prefix):
        data['CI'] = line[len(prefix):]


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
        type_ = 'text'
        if field_def['typedef'] == 'num':
            type_ = 'number'
        alignment_ = 'right'
        if field_def.get('alignment') == 'left':
            alignment_ = 'left'
        return {
            'value': lin,
            'length': field_length,
            'type': type_,
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
    return record


def get_record_type_def(line, def_):
    code_ = line[:2]
    record_def = get_record_def_by_code(code_, def_)
    return record_def


def add_to_meta_lines(lines, data):
    for line in lines:
        if line.startswith('#'):
            # parse some info to display in the page header
            add_meta(line[2:], data)


def add_to_records(lines, data, version):
    def_ = get_exchange_def(version)
    field_defs_ = get_field_def(version)
    for line in lines:
        if not line.startswith('#'):
            record_def = get_record_type_def(line, def_)
            record = parse_line(line.strip(), record_def, field_defs_)
            if record:
                data['records'].append(record)


def parse(lines, version):
    # clear_meta_lines()
    data = dict()
    data['version'] = version
    data['records'] = []
    add_to_meta_lines(lines, data)
    add_to_records(lines, data, version)
    return data


def read_exchange_new(filename, dir_):
    with open(dir_ + filename) as fp:
        lines = fp.readlines()
    version = get_version(lines)
    data = parse(lines, version)
    return data
