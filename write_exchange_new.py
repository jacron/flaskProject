from lib.exchange import get_exchange_def, get_field_def, \
    get_record_def_by_code


def to_line(arr):
    line = ''.join(arr)
    return line.strip()


def get_pos(field, record_def):
    for rec in record_def:
        if rec['@name'] == field:
            return rec['@pos']
    return None


def get_field_def_(field, field_defs):
    for f in field_defs['fields']['field']:
        if f['name'] == field:
            return f
    return None


def fill_field(field, value, line, record_def, field_defs):
    pos = get_pos(field, record_def)
    if not pos:
        print(f'No position found for field {field}, value {value}')
        return
    begin = int(pos) - 1
    field_def = get_field_def_(field, field_defs)
    length = int(field_def['length'])
    # alignment = field_def['alignment']
    end = begin + length
    if value == '':
        value = ' ' * length
    line[begin:end] = value.rstrip()


def output_lines(output_data, version):
    def_ = get_exchange_def(version)
    field_defs_ = get_field_def(version)
    lines = []
    for type_ in output_data:
        line = [' '] * 200
        record_def = get_record_def_by_code(type_, def_)
        for field in output_data[type_]:
            fill_field(field, output_data[type_][field], line,
                       record_def, field_defs_)
        lines.append(to_line(line) + '\n')
    return lines


def get_form_output(form):
    output_data = dict()
    for field in form:
        if '.' in field:
            [type_, name] = field.split('.')
            if type_ not in output_data:
                output_data[type_] = dict()
            output_data[type_][name] = form[field]
    return output_data


def read_meta_lines(filename, dir_):
    meta_lines = []
    with open(dir_ + filename) as fp:
        lines = fp.readlines()
    for line in lines:
        if line.startswith('#'):
            meta_lines.append(line)
    return meta_lines


def write_exchange_new2(form, filename, dir_):
    fle = dir_ + filename + '.edited.bl8'
    with open(fle, "w+") as fp:
        fp.write(form['content'])
    print('written content to', fle)


def write_exchange_new(form, filename, dir_):
    meta_lines = read_meta_lines(filename, dir_)
    output_data = get_form_output(form)
    record_lines = output_lines(output_data, form['version'])
    lines = meta_lines[:-1] + record_lines + [meta_lines[-1]]
    fle = dir_ + filename + '.edited.bl8'
    with open(fle, "w+") as fp:
        fp.writelines(lines)
    print('written content to', fle)
