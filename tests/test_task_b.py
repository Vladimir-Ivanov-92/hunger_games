import pytest

from hunger_games.task_b import get_dict_from_two_list

error_message = "Списки не должны быть равны по длине"


@pytest.mark.parametrize("keys, values, expected_result",
                         [([1, 2, 3], ["1", "2", "3", "4"], {1: "1", 2: "2", 3: "3"}),
                          ([2, 1, 3], ["1", "2", "3", "4"], {1: "1", 2: "2", 3: "3"}),
                          ([1, 2, 3, 4], ["1", "2", "3"], {1: "1", 2: "2", 3: "3"}),
                          ([3, 4, 1, 2], ["1", "2", "3"], {1: "1", 2: "2", 3: "3"}),
                          ([-2, -1], ["1", "2", "3"], {-2: "1", -1: "2"})])
def test_get_dict_from_two_list_good(keys, values, expected_result):
    assert get_dict_from_two_list(keys, values) == expected_result


@pytest.mark.parametrize("keys, values, expected_result",
                         [([], ["1", "2", "3", "4"], {}),
                          ([2, 1, 3], [], {})])
def test_get_dict_from_empty_list(keys, values, expected_result):
    assert get_dict_from_two_list(keys, values) == expected_result


@pytest.mark.parametrize("keys, values, expected_result",
                         [([2, 1, 3], ["1", "2", "3"], error_message),
                          ([], [], error_message)])
def test_get_dict_from_equal_list(keys, values, expected_result):
    assert get_dict_from_two_list(keys, values) == expected_result
