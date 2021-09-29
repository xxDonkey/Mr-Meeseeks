import json
import math
import traceback as tb

from collections import namedtuple

def get(file='config.json', named_tuple=True):
    if named_tuple:
        try:
            with open(file, encoding='utf8') as data:
                return json.load(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        except AttributeError:
            raise AttributeError("Unknown argument")
        except FileNotFoundError:
            raise FileNotFoundError("JSON file wasn't found")
    else:
        try:
            with open(file, encoding='utf8') as data:
                return json.load(data)
        except FileNotFoundError:
            raise FileNotFoundError("JSON file wasn't found")

# debug tool
def get_traceback(err, advanced: bool=True):
    trace = ''.join(tb.format_tb(err.__traceback__))
    error = ('```py\n{1}{0}: {2}\n```').format(type(err).__name__, trace, err)
    return error if advanced else f"{type(err).__name__}: {err}"

