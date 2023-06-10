import pytest

from hunger_games.task_d import get_async_requests

error_message_num = "Ошибка! Кол-во запросов должно быть > 0"
error_message_url = "Неверно указан url"


@pytest.mark.parametrize("url, num_of_requests, expected_result",
                         [("https://google.com", 10, "Number of response: 10"),
                          ("https://google.com", 100, "Number of response: 100"),
                          ("https://mail.ru", 50, "Number of response: 50"),
                          ("https://mail.ru", -1, error_message_num),
                          ("https://mail.ru", 0, error_message_num),
                          ("htt/mail.com", 0, error_message_num),
                          ])
def test_get_async_requests(url, num_of_requests, expected_result):
    assert get_async_requests(url, num_of_requests) == expected_result
