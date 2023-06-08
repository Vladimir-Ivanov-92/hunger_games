import pytest

from hunger_games.task_a import get_git_project_title

# Good script______
good_links = [
    "https://github.com/miguelgrinberg/Flask-SocketIO",
    "https://github.com/miguelgrinberg/Flask-SocketIO.git",
    "https://github.com/miguelgrinberg/python-socketio",
    "https://github.com/miguelgrinberg/APIFairy.git",
]

result_for_good_links = "Название проекта: Flask-SocketIO\n" + \
                        "Название проекта: Flask-SocketIO\n" + \
                        "Название проекта: python-socketio\n" + \
                        "Название проекта: APIFairy\n"


@pytest.mark.parametrize("link, expected_result", [(good_links, result_for_good_links)])
def test_get_git_project_title_good(link, expected_result):
    assert get_git_project_title(link) == expected_result


# Fail script______
fail_links = [
    "https://github.com/miguelgrinberg/APIFairy.git/new",
    "https://githubbbbbbb.com/miguelgrinberg/APIFairy.git",
    "https:githubbbbbbb.com/miguelgrinberg/APIFairy.git",
    "https:githubbbbbbb.com/miguelgrinberg/Test1.git/",
    "https://github.com/miguelgrinberg/API-Fairy.new"
    "",
]

message = " не соотвествует формату:'https://github.com/имя пользователя/имя проекта'" \
          " или 'https://github.com/имя пользователя/имя проекта.git'\n"

result_for_fail_links = \
    "Ссылка https://github.com/miguelgrinberg/APIFairy.git/new" + message + \
    "Ссылка https://githubbbbbbb.com/miguelgrinberg/APIFairy.git" + message + \
    "Ссылка https:githubbbbbbb.com/miguelgrinberg/APIFairy.git" + message + \
    "Ссылка https:githubbbbbbb.com/miguelgrinberg/Test1.git/" + message + \
    "Ссылка https://github.com/miguelgrinberg/API-Fairy.new" + message


@pytest.mark.parametrize("link, expected_result", [(fail_links, result_for_fail_links)])
def test_get_git_project_title_bad(link, expected_result):
    assert get_git_project_title(link) == expected_result
