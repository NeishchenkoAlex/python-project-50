def build_diff(parced_data1: dict, parced_data2: dict):
    diff = list()
    sorted_keys = sorted(
        list(set(parced_data1.keys()) | set(parced_data2.keys()))
    )
    for key in sorted_keys:
        if key not in parced_data1:
            diff.append({
                'key': key,
                'operation': 'add',
                'new': parced_data2[key]
            })
        elif key not in parced_data2:
            diff.append({
                'key': key,
                'operation': 'removed',
                'old': parced_data1[key]
            })
        elif isinstance(parced_data1[key], dict) and isinstance(
                parced_data2[key], dict):
            child = build_diff(parced_data1[key], parced_data2[key])
            diff.append({
                'key': key,
                'operation': 'nested',
                'value': child
            })
        elif parced_data1[key] == parced_data2[key]:
            diff.append({
                'key': key,
                'operation': 'same',
                'value': parced_data1[key]
            })
        elif parced_data1[key] != parced_data2[key]:
            diff.append({
                'key': key,
                'operation': 'changed',
                'old': parced_data1[key],
                'new': parced_data2[key]
            })
    return diff 

from typing import Any

DEFAULT_INDENT = 4


def to_str(value: Any, depth: int) -> str:
    if isinstance(value, dict):
        lines = ['{']
        for key, nested_value in value.items():
            if isinstance(nested_value, dict):
                new_value = to_str(nested_value, depth + DEFAULT_INDENT)
                lines.append(f"{' ' * depth}    {key}: {new_value}")
            else:
                lines.append(f"{' ' * depth}    {key}: {nested_value}")
        lines.append(f'{" " * depth}}}')
        return '\n'.join(lines)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def line_forming(dictionary: dict, key: Any, depth: int, sign: str) -> str:
    return f'{" " * depth}{sign}{dictionary["key"]}: ' \
           f'{to_str(dictionary[key], depth + DEFAULT_INDENT)}'


def build_stylish_iter(diff: dict, depth=0) -> str:
    lines = ['{']
    for dictionary in diff:
        if dictionary['operation'] == 'same':
            lines.append(line_forming(
                dictionary, 'value',
                depth, sign='    '
            ))

        if dictionary['operation'] == 'add':
            lines.append(line_forming(
                dictionary, 'new',
                depth, sign='  + '
            ))

        if dictionary['operation'] == 'removed' or dictionary[
                'operation'] == 'changed':
            lines.append(line_forming(
                dictionary, 'old',
                depth, sign='  - '
            ))

        if dictionary['operation'] == 'changed':
            lines.append(
                line_forming(
                    dictionary, 'new',
                    depth, sign='  + '
                ))

        if dictionary['operation'] == 'nested':
            new_value = build_stylish_iter(dictionary['value'],
                                           depth + DEFAULT_INDENT)
            lines.append(
                f'{" " * depth}    {dictionary["key"]}: {new_value}')
    lines.append(f'{" " * depth}}}')
    return '\n'.join(lines)


def render_stylish(diff: dict) -> str:
    return build_stylish_iter(diff)

d1={
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
  }
d2={
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
  }
d3=build_diff(d1,d2)
d4=build_stylish_iter(d3)
print(d4)