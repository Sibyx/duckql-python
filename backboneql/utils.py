import json


def json_parse():
    pass


def json_dumps(**kwargs):
    print(kwargs)
    return json.dumps(**kwargs)


class BaseConfig(object):
    json_dumps = json_dumps
