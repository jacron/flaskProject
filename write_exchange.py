from settings import format_data, sampledir, meta_lines


def get_setting(field):
    for type_ in format_data:
        for item in format_data[type_]:
            if item.get('field'):
                if item['field'] == field:
                    return item
            if item.get('composite'):
                for item2 in item['composite']['fields']:
                    if item2['field'] == field:
                        return item2
    return None


def to_line(arr):
    line = ''.join(arr)
    return line.strip()


def fill_field(field, value, line):
    setting = get_setting(field)
    if setting.get('until'):
        line[setting['begin']:setting['until']] = value
    else:
        line[setting['begin']] = value


def output_lines(output_data):
    lines = []
    for type_ in output_data:
        line = [' '] * 200
        for field in output_data[type_]:
            fill_field(field, output_data[type_][field], line)
        lines.append(to_line(line) + '\n')
    return lines


def get_form_output(form):
    output_data = dict()
    for field in form:
        [type_, name] = field.split('.')
        if type_ not in output_data:
            output_data[type_] = dict()
        output_data[type_][name] = form[field]
    return output_data


def write_exchange(form, filename):
    output_data = get_form_output(form)
    lines = meta_lines + output_lines(output_data)
    fle = sampledir + filename + '.edited.bl8'
    with open(fle, "w+") as fp:
        fp.writelines(lines)
    print('written content to', fle)
