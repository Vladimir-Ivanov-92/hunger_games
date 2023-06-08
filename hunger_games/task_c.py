def get_new_list(item_list: list[int | str]) -> list[int | str] | str:
    """
    Функция принимает список элементов (состоящий из строк и цифр)
    и возвращает новый список, с условием:
    - если элемент списка был строкой, то в начало строки добавляется текст "abc_",
    в конец строки - "_cba".
    - Если элемент был int - то его значение возводится в квадрат.
    """
    error_massage = "Переданны некорректные данные"
    try:
        response = list(
            map(lambda x: x ** 2 if isinstance(x, int) else "abc_" + x + "_cba",
                item_list))
    except TypeError:
        return error_massage
    return response


if __name__ == '__main__':
    item_lists = [1, "1", 2, "2"], [2, 4], ["a", "b"], [], [-2, "python"], [(1, 2), "p"]
    for item in item_lists:
        print(get_new_list(item))
