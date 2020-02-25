import importlib
import json


def custom_parser(data: dict):
    obj = data

    if 'obj' in data:
        bits = data.pop('obj').split('.')

        class_name = bits[1]

        module_ = importlib.import_module(f"backboneql.{bits[0]}")
        class_ = getattr(module_, class_name)

        obj = class_(**data)

    return obj


def json_parse(s, **kwargs):
    kwargs['object_hook'] = custom_parser
    return json.loads(s, **kwargs)
