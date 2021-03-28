from settings import format_data, sampledir


def add_meta(line, data):
    prefix = '$Vn: '
    if line.startswith(prefix):
        data['Version'] = line[len(prefix):]
    prefix = '$NR: '
    if line.startswith(prefix):
        data['CI'] = line[len(prefix):]


def parse_record(line):
    record = dict()
    for frmt in format_data['general']:
        if len(frmt) == 3:
            record[frmt[0]] = line[frmt[1]:frmt[2]]
        else:
            record[frmt[0]] = line[frmt[1]]
    extra = dict()
    for frmt in format_data[record['type']]:
        if len(frmt) == 3:
            extra[frmt[0]] = line[frmt[1]:frmt[2]]
        else:
            extra[frmt[0]] = line[frmt[1]]
    record['extra'] = extra
    return record


def parse(lines):
    data = dict()
    data['records'] = []
    format_data['meta_lines'] = []
    for line in lines:
        if line.startswith('#'):
            format_data['meta_lines'].append(line)
            add_meta(line[2:], data)
        else:
            data['records'].append(parse_record(line))
    return data


def read_exchange(filename):
    with open(sampledir + filename) as fp:
        lines = fp.readlines()
        data = parse(lines)
    return data
