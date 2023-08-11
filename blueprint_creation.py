import base64
import copy
import json
import zlib

from values import Var
from values import Const
from signals_types import signal_type_dict


class OpInfo:
    def __init__(self, delay, flt=None):
        self.delay = delay
        self.flt = flt


coded_str = "0eNqNksFugzAMht/F56QSFEbLi+xQVVUAb7MWHBZMtQrx7kuK1HGgG0dbvz/7tz1CZQfsPLFAOQLVjnsoTyP09M7GxpzcOoQSSLAFBWzaGEWdGBZdu" \
            "7YiNuI8TAqIG/yGMpnOCpCFhHDG3YPbhYe2Qh8Ef4IUdK4PtY5j/8DLil2u4AalTvJdHvo05LGeBamKDPHOXir8MFcKgFD1RlbQP/FyJS9DyDymmBX" \
            "6NXqo3RCXkSzcqH/3Qd6x7qwRXCLSByPdwLCGmzC2XR1ivwHgXf2JonuybpWRbWD8vsMaId9A6J01XneG0Wr8Gqhr8QntZTpP8VPu9cvWCq7hdvN5D0lWHNOi2BfH/JBN0w/cpuTU"

template_combinator = {
    "entity_number": 1,
    "name": "constant-combinator",
    "position": {
        # "x": 48.5,
        # "y": -14.5
        "x": 0.5,
        "y": 0.5
    },
    "direction": 2,
    "control_behavior": {
        "filters": [
            {
                "signal": {
                    "type": "virtual",
                    "name": "signal-L"
                },
                "count": 1,
                "index": 1
            }
        ]
    }
}

template_filter = template_combinator['control_behavior']['filters'][0]


def get_letter_filter(letter: str, count=0):
    # TODO check if it is really a letter?
    flt = copy.deepcopy(template_filter)
    flt['signal']['name'] = f"signal-{letter}"
    flt['count'] = count
    return flt


global_scope_start = 1

op_info_table = {
    'write': OpInfo(3),
    'write_add': OpInfo(3),
    'jump': OpInfo(4),
    'c_jump': OpInfo(8),
    '*': OpInfo(3, get_letter_filter('A', 1)),
    '/': OpInfo(3, get_letter_filter('A', 2)),
    '%': OpInfo(3, get_letter_filter('A', 5)),
    'exp': OpInfo(3, get_letter_filter('A', 6)),
    '<<': OpInfo(3, get_letter_filter('A', 7)),
    '>>': OpInfo(3, get_letter_filter('A', 8)),
    '&': OpInfo(3, get_letter_filter('A', 9)),
    '|': OpInfo(3, get_letter_filter('A', 10)),
    '^': OpInfo(3, get_letter_filter('A', 11)),
    # TODO add conversion
    '==': OpInfo(4, get_letter_filter('A', 13)),
    '!=': OpInfo(4, get_letter_filter('A', 14)),
    '<': OpInfo(4, get_letter_filter('A', 15)),
    '<=': OpInfo(4, get_letter_filter('A', 16)),
    '>': OpInfo(4, get_letter_filter('A', 17)),
    '>=': OpInfo(4, get_letter_filter('A', 18)),
}
# op_action = list(filter(lambda info: info.flt is not None, op_info_table.values()))
op_action = {op: info for (op, info) in op_info_table.items() if info.flt is not None}


def enumerate_commands(command_list):
    line_number = 1
    for command in command_list:
        command['line_num'] = line_number
        if 'op' in command:
            line_number += 1


def create_blueprint(command_list: list):
    enumerate_commands(command_list)

    filters_list = []
    for command in command_list:
        if 'op' in command:
            filters_list.append(command_to_filters(command))

    combinators = []
    for i in range(len(filters_list)):
        combinator = copy.deepcopy(template_combinator)
        combinator['entity_number'] = i + 1
        combinator['position']['y'] += i
        combinator['control_behavior']['filters'] = filters_list[i]
        combinators.append(combinator)

    zlib_str = base64.b64decode(coded_str[1:])
    json_str = zlib.decompress(zlib_str)
    blueprint = json.loads(json_str)

    blueprint["blueprint"]["entities"] = combinators

    json_str = json.dumps(blueprint)
    zlib_str = zlib.compress(json_str.encode())
    result = base64.b64encode(zlib_str)

    return '0' + result.decode()


def command_to_filters(command):
    filters = []
    op = command['op']

    if op == 'write' or op == 'write_add':
        to = command['to']
        addr = to.addr
        if to.scope == 'global':
            if (addr + global_scope_start) == 0:
                raise Exception("Trying to access memory 0")
            filters.append(get_letter_filter('W', addr + global_scope_start))
        elif to.scope == 'local':
            filters.append(get_letter_filter('P', 1))  # stack pointer
            if addr != 0:
                filters.append(get_letter_filter('W', addr))
        if op == 'write_add':
            filters.append(get_letter_filter('A', 3))
    elif op == 'c_jump':
        # TODO add jump to value in register
        label = command['destination']
        filters.append(get_letter_filter('J', label['line_num']))

        condition = command['condition']
        if condition == 'is_zero':
            filters.append(get_letter_filter('C', 1))
        # TODO add other conditions
    elif op == 'jump':
        label = command['destination']
        filters.append(get_letter_filter('G', label['line_num']))
    elif op in op_action:
        filters.append(op_info_table[op].flt)

    if 'from' in command:
        parse_from_field(command['from'], filters)

    filters.append(get_letter_filter('D', op_info_table[op].delay))

    # filters indexing
    for i in range(len(filters)):
        filters[i]['index'] = i + 1

    return filters


def parse_from_field(frm, filters: list):
    output_list = []
    if isinstance(frm, tuple):
        output_list.extend(frm)
    else:
        output_list.append(frm)

    for out in output_list:
        if isinstance(out, Var):
            addr = out.addr
            if out.scope == 'global':
                if (addr + global_scope_start) == 0:
                    raise Exception("Trying to access memory 0")
                filters.append(get_letter_filter('O', addr + global_scope_start))
            elif out.scope == 'local':
                filters.append(get_letter_filter('U', 1))  # stack pointer
                if addr != 0:
                    filters.append(get_letter_filter('O', addr))
            else:
                raise Exception("Unknown scope")

        elif isinstance(out, Const):
            for signal_name, count in out.items():
                if signal_name == 'raw':
                    signal_name = 'signal-dot'
                    signal_type = 'virtual'
                elif signal_type_dict.get(signal_name) is not None:
                    signal_type = signal_type_dict[signal_name]
                else:
                    raise Exception(f"Unknown signal {signal_name}")
                flt = copy.deepcopy(template_filter)
                flt['signal']['name'] = signal_name
                flt['signal']['type'] = signal_type
                flt['count'] = count
                filters.append(flt)
