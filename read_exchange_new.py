import xmltodict as xmltodict

exchange_defs = {
    '6': './defs/fexchange-v6.xml',
    '7': './defs/fexchange-v7.xml'
}
field_defs = {
    '6': './defs/field-defs-v6.xml',
    '7': './defs/field-defs-v7.xml'
}


def get_exchange_def(version):
    def_ = exchange_defs.get(version)
    if not def_:
        return None
    with open(def_, 'rb') as fp:
        return xmltodict.parse(fp)


def get_field_def(version):
    def_ = field_defs.get(version)
    if not def_:
        return None
    with open(def_, 'rb') as fp:
        return xmltodict.parse(fp)


def get_record_def(code, def_):
    for rec in def_['records']['record']:
        if rec['@code'] == code:
            return rec['field']


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
    record_def = get_record_def(code_, def_)
    return record_def


def parse(lines, version):
    def_ = get_exchange_def(version)
    field_defs_ = get_field_def(version)
    data = dict()
    data['records'] = []
    for line in lines:
        if not line.startswith('#'):
            record_def = get_record_type_def(line, def_)
            record = parse_line(line.strip(), record_def, field_defs_)
            if record:
                data['records'].append(record)
    return data


def get_version(lines):
    version_prefix = '# $Vn: Exchange Format '
    len_pre = len(version_prefix)
    for line in lines:
        lstripped = line.strip()
        if lstripped.startswith(version_prefix):
            return lstripped[len_pre:]
    return None


def read_exchange_new(filename, dir_):
    with open(dir_ + filename) as fp:
        lines = fp.readlines()
    version = get_version(lines)
    data = parse(lines, version)
    return data
