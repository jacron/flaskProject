from settings import format_data, sampledir


def add_meta(line, data):
    prefix = '$Vn: '
    if line.startswith(prefix):
        data['Version'] = line[len(prefix):]
    prefix = '$NR: '
    if line.startswith(prefix):
        data['CI'] = line[len(prefix):]


def parse_record(line, format_data_):
    record = dict()
    for frmt in format_data_:
        if frmt.get('until'):
            record[frmt['field']] = line[frmt['begin']:frmt['until']]
        else:
            record[frmt['field']] = line[frmt['begin']]
    return record


def parse_line(line):
    record = parse_record(line, format_data['general'])
    record['extra'] = parse_record(line, format_data[record['type']])
    return record


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
            data['records'].append(parse_line(line))
    return data


def read_exchange(filename):
    with open(sampledir + filename) as fp:
        lines = fp.readlines()
        data = parse(lines)
    return data
