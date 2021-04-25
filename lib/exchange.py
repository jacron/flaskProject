import xmltodict as xmltodict


exchange_defs = {
    '6': './defs/fexchange-v6.xml',
    '7': './defs/fexchange-v7.xml'
}
field_defs = {
    '6': './defs/field-defs-v6.xml',
    '7': './defs/field-defs-v7.xml'
}


def get_version(lines):
    version_prefix = '# $Vn: Exchange Format '
    len_pre = len(version_prefix)
    for line in lines:
        lstripped = line.strip()
        if lstripped.startswith(version_prefix):
            return lstripped[len_pre:]
    return None


def get_exchange_def(version):
    def_ = exchange_defs.get(version)
    if not def_:
        return None
    with open(def_, 'rb') as fp:
        return xmltodict.parse(fp)


def get_field_def(version):
    def_ = field_defs.get(version)
    if not def_:
        return None
    with open(def_, 'rb') as fp:
        return xmltodict.parse(fp)


def get_record_def_by_code(code, def_):
    for rec in def_['records']['record']:
        if rec['@code'] == code:
            return rec['field']


