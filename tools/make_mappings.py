"""
Make mappings
use definition file (v7)
to create parts of json validators file
"""
import xmltodict
import json

type_ = 'Af'


def write_json(filename, data):
    with open(filename, 'w') as fp:
        json.dump(data, fp, indent=4)


def get_exchange_def():
    with open('../defs/field-defs-v7.xml', 'rb') as fp:
        return xmltodict.parse(fp)


def get_type(field_):
    if field_['typedef'] == 'char':
        return 'string'
    if field_['typedef'] == 'num':
        if field_['precision'] == '0':
            return 'int'
        else:
            return 'float'


def get_types(def_):
    types = set()
    for field in def_['fields']['field']:
        name = field['name'].split('/')
        if len(name) > 1:
            types.add(name[0])
    return types


def get_validators(def_):
    validators = list()
    for field in def_['fields']['field']:
        name = field['name'].split('/')
        if len(name) > 1:
            if name[0] == type_:
                validators.append({
                    "field": name[1],
                    "column": name[1].upper(),
                    "type": get_type(field)
                })
    return validators


def main():
    def_ = get_exchange_def()
    types = get_types(def_)
    # v7: {'Hl', 'Pn', 'Cl', 'Cm', 'St', 'CT', 'Af', 'Sh', 'Ss', 'Gu'}
    # v6: {'Cm', 'Pn', 'Cl', 'Ss', 'Gu', 'Sh', 'CT', 'Hl', 'St'}
    table = dict()
    table['type'] = type_
    table['table'] = ""
    table['validators'] = get_validators(def_)
    write_json(type_ + '_validators.json', table)


if __name__ == "__main__":
    main()
