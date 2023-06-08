from collections.abc import Hashable
from typing import Any


def get_dict_from_two_list(keys: list[Hashable], values: list[Any]) -> dict | str:
    """
    Функция, принимает два списка и возвращающет словарь (ключ из первого
    списка, значение из второго), упорядоченный по ключам. Проводится проверка
    неравенства длин принимаемых списков.
    """
    response = {}
    error_message = "Списки не должны быть равны по длине"

    if len(keys) == len(values):
        return error_message
    else:
        keys.sort()
        gen_key = (i for i in keys)
        gen_value = (i for i in values)
        try:
            while True:
                response[next(gen_key)] = next(gen_value)
        except StopIteration:
            pass
    return response


if __name__ == '__main__':

    keys = [1, 2, 3], [2, 1, 3], [1, 2, 3, 4], [3, 4, 1, 2], [-2, -1], []
    values = ["1", "2", "3", "4"]
    for k in keys:
        print(get_dict_from_two_list(k, values))

    keys = [1, 2, 3, 4]
    values = ["1", "2", "3"], ["1", "2", "3", "4"], ["1", "2", "3", "4", "5"], []
    for v in values:
        print(get_dict_from_two_list(keys, v))

    keys = []
    values = []
    print(get_dict_from_two_list(keys, values))
