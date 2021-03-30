from settings import format_data, sampledir


def add_meta(line, data):
    prefix = '$Vn: '
    if line.startswith(prefix):
        data['Version'] = line[len(prefix):]
    prefix = '$NR: '
    if line.startswith(prefix):
        data['CI'] = line[len(prefix):]


def parse_general(record, line):
    for frmt in format_data['general']:
        if len(frmt) == 3:
            record[frmt[0]] = line[frmt[1]:frmt[2]]
        else:
            record[frmt[0]] = line[frmt[1]]


def parse_extra(extra, record, line):
    try:
        for frmt in format_data[record['type']]:
            if len(frmt) == 3:
                extra[frmt[0]] = line[frmt[1]:frmt[2]]
            else:
                extra[frmt[0]] = line[frmt[1]]
    except IndexError as e:
        print(e)
        print(line, frmt[0], frmt[1])


def parse_record(line):
    record = dict()
    parse_general(record, line)
    extra = dict()
    parse_extra(extra, record, line)
    record['extra'] = extra
    return record


def parse(lines):
    data = dict()
    data['records'] = []
    format_data['meta_lines'] = []
    for line in lines:
        if line.startswith('#'):
            # save for writing the output
            format_data['meta_lines'].append(line)
            # parse for some info to display
            add_meta(line[2:], data)
        else:
            # parse record to use in the edit box in the form
            data['records'].append(parse_record(line))
    return data


def read_exchange(filename):
    with open(sampledir + filename) as fp:
        lines = fp.readlines()
        data = parse(lines)
    return data
