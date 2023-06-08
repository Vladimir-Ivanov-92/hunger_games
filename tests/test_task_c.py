import pytest

from hunger_games.task_c import get_new_list

error_message = "Переданны некорректные данные"


@pytest.mark.parametrize("item_list, expected_result",
                         [([1, "1", 2, "2"], [1, 'abc_1_cba', 4, 'abc_2_cba']),
                          ([2, 4], [4, 16]),
                          (["a", "b"], ['abc_a_cba', 'abc_b_cba']),
                          ([-2, "python"], [4, 'abc_python_cba']),
                          ([], [])])
def test_get_new_list_good(item_list, expected_result):
    assert get_new_list(item_list) == expected_result


@pytest.mark.parametrize("item_list, expected_result",
                         [([(1, 2), "p"], error_message),
                          ([{1: "1"}, 1], error_message)])
def test_get_new_list_invalid_data(item_list, expected_result):
    assert get_new_list(item_list) == expected_result
