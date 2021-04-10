from settings import format_data, sampledir


def add_meta(line, data):
    prefix = '$Vn: '
    if line.startswith(prefix):
        data['Version'] = line[len(prefix):]
    prefix = '$NR: '
    if line.startswith(prefix):
        data['CI'] = line[len(prefix):]


def record_value(line, frmt):
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
    return {
        "label": frmt['label'],
        "fields": fields
    }


def parse_record(line, format_data_):
    frmt = None
    try:
        record = dict()
        for frmt in format_data_:
            if frmt.get('composite'):
                key = '#' + frmt['composite']['label']
                record[key] = composite_record_values(line,
                                                      frmt['composite'])
            else:
                record[frmt['field']] = {
                    "value": record_value(line, frmt)
                }
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
    format_data['meta_lines'] = []
    for line in lines:
        if line.startswith('#'):
            # save meta-line for writing to the output file
            format_data['meta_lines'].append(line)
            # parse some info to display in the page header
            add_meta(line[2:], data)
        else:
            # parse record to use in the edit box in the form
            record = parse_line(line)
            if record:
                data['records'].append(parse_line(line))
    return data


def read_exchange(filename):
    with open(sampledir + filename) as fp:
        lines = fp.readlines()
        data = parse(lines)
    return data
