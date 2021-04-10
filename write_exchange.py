from settings import format_data, sampledir


def write_exchange(form, filename):
    # first use saved (unedited) 'comment' lines
    lines = format_data['meta_lines']
    output_data = dict()
    # now use the edited data in the form
    # collect the data
    for field in form:
        [type_, name] = field.split('.')
        if type_ not in output_data:
            output_data[type_] = dict()
        output_data[type_][name] = form[field]
    # put the data in lines
    for type_ in output_data:
        line = ''
        for field in output_data[type_]:
            line += output_data[type_][field]
            if field == 'time':
                if type_ == 'Pn':
                    line += ' ' * 20
                else:
                    line += ' ' * 43
        lines.append(line + '\n')

    fle = sampledir + filename + '.edited.bl8'
    with open(fle, "w+") as fp:
        fp.writelines(lines)

    print('written content to', fle)
