from settings import format_data, meta_lines, clear_meta_lines


def add_meta(line, data):
    prefix = '$Vn: '
    if line.startswith(prefix):
        data['Version'] = line[len(prefix):]
    prefix = '$NR: '
    if line.startswith(prefix):
        data['CI'] = line[len(prefix):]


def record_value(line, frmt):
    if len(line) < frmt['begin'] + 2:
        if frmt.get('until'):
            return ' ' * (frmt['until'] - frmt['begin'])
        else:
            return ' '
    if frmt.get('until'):
        return line[frmt['begin']:frmt['until']]
    else:
        return line[frmt['begin']]


def composite_record_values(line, frmt):
    fields = {}
    for field in frmt['fields']:
        fields[field['field']] = {
            "value": record_value(line, field)
        }
    nullable = frmt.get('nullable', True)
    return {
        "label": frmt['label'],
        "nullable": nullable,
        "fields": fields
    }


def composite_record(record, line, frmt):
    key = '#' + frmt['composite']['label']
    record[key] = composite_record_values(line, frmt['composite'])


def simple_record(record, line, frmt):
    nullable = frmt.get('nullable', True)
    record[frmt['field']] = {
        "value": record_value(line, frmt),
        "nullable": nullable
    }


def parse_record(line, format_data_):
    frmt = None
    try:
        record = dict()
        for frmt in format_data_:
            if frmt.get('composite'):
                composite_record(record, line, frmt)
            else:
                simple_record(record, line, frmt)
    except TypeError as e:
        print(e)
        print(frmt)
        record = None
    return record


def parse_line(line):
    record = parse_record(line, format_data['general'])
    extra = parse_record(line, format_data[record['type']['value']])
    return {**record, **extra}


def parse(lines):
    data = dict()
    data['records'] = []
    clear_meta_lines()
    for line in lines:
        if line.startswith('#'):
            # save meta-line for writing to the output file
            meta_lines.append(line)
            # parse some info to display in the page header
            add_meta(line[2:], data)
        else:
            # parse record to use in the edit box in the form
            record = parse_line(line)
            if record:
                data['records'].append(record)
    return data


def read_exchange(filename, dir_):
    with open(dir_ + filename) as fp:
        lines = fp.readlines()
        data = parse(lines)
    return data
