def get_git_project_title(links: list[str]) -> str:
    """
    Функция принимает в качестве аргумента набор ссылок. Ссылки имеют формат ссылок
    на проекты на гитхабе. Функция обрабатвает полученные ссылки и возвращает
    названия самих гит-проектов или сообщение об ошибке, при получении ссылки
    "вне формата".
    """
    error_message = "Ссылка {link} не соотвествует формату:" \
                    "'https://github.com/имя пользователя/имя проекта' или " \
                    "'https://github.com/имя пользователя/имя проекта.git'"

    response_message = "Название проекта: {}"

    response = str()

    for link in links:
        if not link.startswith("https://github.com/") or len(link.split("/")) != 5:
            response += error_message.format(link=link) + "\n"
        else:
            raw_title = link.split("/")[-1].split(".")
            if (len(raw_title) == 2 and raw_title[1] == "git") or len(raw_title) == 1:
                git_project_title = raw_title[0]
                response += response_message.format(git_project_title) + "\n"
            else:
                response += error_message.format(link=link) + "\n"
    return response


if __name__ == '__main__':
    github_links = [
        "https://github.com/miguelgrinberg/Flask-SocketIO",
        "https://github.com/miguelgrinberg/Flask-SocketIO.git",
        "https://github.com/miguelgrinberg/python-socketio",
        "https://github.com/miguelgrinberg/APIFairy.git",
        "https://github.com/miguelgrinberg/APIFairy.git/new",
        "https://githubbbbbbb.com/miguelgrinberg/APIFairy.git",
        "https:githubbbbbbb.com/miguelgrinberg/APIFairy.git",
        "https:githubbbbbbb.com/miguelgrinberg/Test1.git/",
        "https://github.com/miguelgrinberg/API-Fairy.new"
        "",
    ]

    print(get_git_project_title(github_links))
