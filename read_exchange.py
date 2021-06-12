import os.path
from collections import OrderedDict

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
        if field_length > 20:
            field_length = 21
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
            'alignment': alignment_,
            'position': begin
        }
    except Exception as e:
        print(e)
        print(rec)
        print(f'length of line={len(line)}')
        return None


def parse_line(line, record_def, field_defs_):
    record = dict()
    fields = OrderedDict()
    for rec in record_def:
        field = get_field(rec, field_defs_, line)
        if field:
            fields[rec['@name']] = field
    record['fields'] = fields
    record['name'] = names[fields['type']['value']]
    return record


def get_record_type_def(line, def_):
    code_ = line[:2]
    # let's try: Sm really is Hl
    if code_ == 'Sm':
        code_ = 'Hl'
    record_def = get_record_def_by_code(code_, def_)
    if not record_def:
        print('No record def for code: ' + code_)
    return record_def


def get_meta(line, meta):
    parts = line[2:].split(': ')
    prefix = parts[0][1:]
    value = parts[1]
    meta[prefix] = value


def get_record(line, records, def_, field_defs_, codes, code, i):
    record_def = get_record_type_def(line, def_)
    if record_def:
        record = parse_line(line.strip(), record_def, field_defs_)
        if record:
            rcode = record['fields']['type']['value']
            codes.add(rcode)
            if code is None or rcode in code:
                record['nr'] = i
                records.append(record)


def get_records(lines, def_, field_defs_, code):
    records = []
    meta = dict()
    i = 1
    codes = set()
    for line in lines:
        if line.startswith('#'):
            get_meta(line, meta)
        else:
            get_record(line, records, def_, field_defs_, codes, code, i)
        i += 1
    return records, meta, codes


def read_exchange(filename, dir_, code):
    path = os.path.join(dir_, filename)
    data = dict()
    try:
        with open(path) as fp:
            lines = fp.readlines()
        version = get_version(lines)
        def_ = get_exchange_def(version)
        field_defs_ = get_field_def(version)
        data['lines'] = lines
        data['records'], data['meta'], data['codes'] = \
            get_records(lines, def_, field_defs_, code)
        data['version'] = version
    except FileNotFoundError as e:
        print(e)
    return data
