import pytest

from hunger_games.task_e import Text

test_text_1 = """Написать класс, принимающий на вход текст. Один метод класса 
    должен выводить в консоль самое длинное слово в тексте. Второй метод - самое часто 
    встречающееся слово. Третий метод выводит количество спецсимволов в тексте 
    (точки, запятые и так далее). Четвертый метод выводит все палиндромы через запятую.
    """
test_text_2 = """Реализовать функцию, принимающую два списка и возвращающую 
    словарь (ключ из первого списка, значение из второго), упорядоченный по ключам. 
    Длина первого списка не должна быть равна длине второго. 
    """

test_text_3 = "Дед искал довод, но заказ получил казак, поэтому устроил топот"

test_text_4 = ""


@pytest.mark.parametrize("text, expected_result", [(test_text_1, "встречающееся"),
                                                   (test_text_2, "упорядоченный"),
                                                   (test_text_3, "получил"),
                                                   (test_text_4, "")])
def test_get_longest_word(text, expected_result):
    assert Text(text).get_longest_word() == expected_result


@pytest.mark.parametrize("text, expected_result", [(test_text_1, "метод"),
                                                   (test_text_2, "списка"),
                                                   (test_text_4, "")])
def test_get_most_common_word(text, expected_result):
    assert Text(text).get_most_common_word() == expected_result


@pytest.mark.parametrize("text, expected_result", [(test_text_1, 10),
                                                   (test_text_2, 7),
                                                   (test_text_4, 0)])
def test_get_number_of_special_characters(text, expected_result):
    assert Text(text).get_number_of_special_characters() == expected_result


@pytest.mark.parametrize("text, expected_result", [(test_text_3,
                                                    "дед, довод, заказ, казак, топот"),
                                                   (test_text_4, "")])
def test_get_number_of_special_characters(text, expected_result):
    assert Text(text).get_all_palindromes() == expected_result
