import importlib
import json

from duckql.exceptions import ParseError


def custom_parser(data: dict):
    obj = data

    if 'obj' in data:
        bits = data.pop('obj').split('.')

        try:
            module_name = f"duckql.{bits[0]}"
            class_name = bits[1]
        except IndexError:
            raise ParseError("Invalid object!")

        module_ = importlib.import_module(module_name)
        class_ = getattr(module_, class_name)

        obj = class_(**data)

    return obj


def json_parse(s, **kwargs):
    kwargs['object_hook'] = custom_parser
    return json.loads(s, **kwargs)
