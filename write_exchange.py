from settings import format_data, sampledir


def write_exchange(form, filename):
    lines = format_data['meta_lines']
    output_data = dict()
    for field in form:
        [type_, name] = field.split('.')
        if type_ not in output_data:
            output_data[type_] = dict()
        output_data[type_][name] = form[field]
    for type_ in output_data:
        line = ''
        for field in output_data[type_]:
            line += output_data[type_][field]
            if field == 'time':
                if type_ == 'Pn':
                    line += ' ' * 19
                else:
                    line += ' ' * 42
        lines.append(line + '\n')

    with open(sampledir + filename + '.testing', "w+") as fp:
        fp.writelines(lines)
