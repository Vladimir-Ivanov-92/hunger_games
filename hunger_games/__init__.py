from hunger_games.task_a import get_git_project_title
from hunger_games.task_b import get_dict_from_two_list
from hunger_games.task_c import get_new_list
from hunger_games.task_d import get_async_requests
from hunger_games.task_e import Text


def task_a():
    """
    test_case:
     github_links = [
            "https://github.com/miguelgrinberg/Flask-SocketIO",
            "https://github.com/miguelgrinberg/Flask-SocketIO.git",
            "https://github.com/miguelgrinberg/python-socketio",
            "https://github.com/miguelgrinberg/APIFairy.git",
            "https://github.com/miguelgrinberg/APIFairy.git/new",
            "https://githubbbbbbb.com/miguelgrinberg/APIFairy.git",
            "https:githubbbbbbb.com/miguelgrinberg/APIFairy.git",
            "https:githubbbbbbb.com/miguelgrinberg/Test1.git/",
            "https://github.com/miguelgrinberg/API-Fairy.new",
            "",
        ]
    """

    github_links = [
        "https://github.com/miguelgrinberg/Flask-SocketIO",
        "https://github.com/miguelgrinberg/Flask-SocketIO.git",
        "https://github.com/miguelgrinberg/python-socketio",
        "https://github.com/miguelgrinberg/APIFairy.git",
        "https://github.com/miguelgrinberg/APIFairy.git/new",
        "https://githubbbbbbb.com/miguelgrinberg/APIFairy.git",
        "https:githubbbbbbb.com/miguelgrinberg/APIFairy.git",
        "https:githubbbbbbb.com/miguelgrinberg/Test1.git/",
        "https://github.com/miguelgrinberg/API-Fairy.new",
        "",
    ]

    print(get_git_project_title(github_links))


def task_b_case_1():
    """
        test_case:
            keys = [1, 2, 3], [2, 1, 3], [1, 2, 3, 4], [3, 4, 1, 2], [-2, -1], []
            values = ["1", "2", "3", "4"]
    """
    keys = [1, 2, 3], [2, 1, 3], [1, 2, 3, 4], [3, 4, 1, 2], [-2, -1], []
    values = ["1", "2", "3", "4"]

    for k in keys:
        print(get_dict_from_two_list(k, values))


def task_b_case_2():
    """
        test_case:
            keys = [1, 2, 3, 4]
            values = ["1", "2", "3"], ["1", "2", "3", "4"], ["1", "2", "3", "4", "5"], []
    """
    keys = [1, 2, 3, 4]
    values = ["1", "2", "3"], ["1", "2", "3", "4"], ["1", "2", "3", "4", "5"], []

    for v in values:
        print(get_dict_from_two_list(keys, v))


def task_b_case_3():
    """
        test_case:
            keys = []
            values = []
    """
    keys = []
    values = []
    print(get_dict_from_two_list(keys, values))


def task_c():
    """
        test_case:
            items= [1, "1", 2, "2"], [2, 4], ["a", "b"], [], [-2, "python"], [(1, 2), "p"]
    """
    items = [1, "1", 2, "2"], [2, 4], ["a", "b"], [], [-2, "python"], [(1, 2), "p"]

    for item in items:
        print(get_new_list(item))


def task_d():
    """
        test_case:
            url_1 = "https://google.com"
            url_2 = "http://httpbin.org/delay/3"
    """
    url_1 = "https://google.com"
    url_2 = "http://httpbin.org/delay/3"

    num_of_requests = 100

    print(get_async_requests(url_1, num_of_requests))
    print(get_async_requests(url_2, num_of_requests))


def task_e_get_longest_word():
    """
        test_case:
            text_1 = Написать класс, принимающий на вход текст. Один метод класса должен
            выводить в консоль самое длинное слово в тексте. Второй метод - самое часто
            встречающееся слово. Третий метод выводит количество спецсимволов в тексте
            (точки, запятые и так далее). Четвертый метод выводит все палиндромы через
            запятую.
    """
    text_1 = """Написать класс, принимающий на вход текст. Один метод класса должен \
            выводить в консоль самое длинное слово в тексте. Второй метод - самое часто \
            встречающееся слово. Третий метод выводит количество спецсимволов в тексте \
            (точки, запятые и так далее). Четвертый метод выводит все палиндромы через \
            запятую."""

    # Cамое длинное слово в тексте:
    print(f"Cамое длинное слово в text_1: {Text(text_1).get_longest_word()}",
          end="\n\n")


def task_e_get_most_common_word():
    """
        test_case:
            text_2 = "Принимающий класс. Написать класс, принимающий на вход и текст
                        и цифры."
    """

    text_2 = "Принимающий класс. Написать класс, принимающий на вход и текст и цифры."

    # Cамое часто встречающееся слово:
    print(f"Cамое часто встречающееся слово в text_2: "
          f"{Text(text_2).get_most_common_word()}", end="\n\n")


def task_e_get_number_of_special_characters():
    """
        test_case:
            text_1 = Написать класс, принимающий на вход текст. Один метод класса должен
            выводить в консоль самое длинное слово в тексте. Второй метод - самое часто
            встречающееся слово. Третий метод выводит количество спецсимволов в тексте
            (точки, запятые и так далее). Четвертый метод выводит все палиндромы через
            запятую.
    """

    text_1 = """Написать класс, принимающий на вход текст. Один метод класса должен \
            выводить в консоль самое длинное слово в тексте. Второй метод - самое часто \
            встречающееся слово. Третий метод выводит количество спецсимволов в тексте \
            (точки, запятые и так далее). Четвертый метод выводит все палиндромы через \
            запятую."""

    # Количество спецсимволов в тексте:
    print(f"Количество спецсимволов в text_1: "
          f"{Text(text_1).get_number_of_special_characters()}", end="\n\n")


def task_e_get_all_palindromes():
    """
        test_case:
            text_3 = "Дед искал довод, но заказ получил казак, поэтому устроил топот"
    """

    text_3 = "Дед искал довод, но заказ получил казак, поэтому устроил топот"

    # Все паллиндромы в тексте:
    print(f"Все паллиндромы в text_3: {Text(text_3).get_all_palindromes()}", end="\n\n")


