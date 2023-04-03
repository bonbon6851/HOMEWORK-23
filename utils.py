from typing import Iterable


def read_file(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        data = file.readlines()
        return data


def filter_query(value: str, data: Iterable[str]):
    result = filter(lambda x: value in x, data)
    return result


def map_query(value: str, data: Iterable[str]):
    col_number = int(value)
    result = map(lambda x: x.split(" ")[col_number], data)
    return result


def unique_query(data: str, *args, **kwargs):
    return set(data)


def sorted_query(value: str, data: Iterable[str]):
    reverse = value == 'desk'
    return sorted(data, reverse=reverse)


def limit_query(value: str, data: Iterable[str]):
    limit = int(value)
    return list(data)[:limit]
