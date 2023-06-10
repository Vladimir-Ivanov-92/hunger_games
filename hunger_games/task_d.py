import asyncio
import time
from collections.abc import Sequence

import aiohttp
from aiohttp import ClientResponse, ClientSession, InvalidURL


def runtime(func):
    """
    Декоратор измеряющий время работы функции. Выводит в консоль сообщение
    с временем работы функции.
    """

    def wrapper(*args, **kwargs):
        print(f"Выполняется функция {func.__name__} ....")
        start_timestamp = time.time()
        func_result = func(*args, **kwargs)
        task_time = round(time.time() - start_timestamp, 2)
        print(
            f"\nTotal time work function: '{func.__name__}' is  {task_time} s;"
        )
        return func_result

    return wrapper


async def _get_response(session: ClientSession, url: str,
                        num_task: int) -> ClientResponse | str:
    """
    Отправляет запрос на сервер, и возвращает полученный ответ.
    """
    async with session.get(url) as response:
        print(f"{num_task}", end=" ")
        return response


async def _send_all_requests(url: str, num_of_requests: int) -> Sequence:
    """
    Собирает в tasks все задания и отправляет на исполнение.
    Полученные ответы добавляет в results.
    """
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(num_of_requests):
            num_task = i + 1
            task = asyncio.create_task(_get_response(session, url, num_task))
            tasks.append(task)
        print(f"отправлено {len(tasks)} запросов на адрес {url}")
        print("получен ответ от запроса №:")
        results = await asyncio.gather(*tasks)
    return results


@runtime
def get_async_requests(url: str, num_of_requests: int) -> str:
    """
    Отправляет асинхронно n запросов по заданному адресу.
    Возвращает сообщение с кол-вом полученных ответов. С помощью декоратора @runtime
    в консоль выводится сообщение с временем работы функции.
    """
    error_message_num = "Ошибка! Кол-во запросов должно быть > 0"
    error_message_url = "Неверно указан url"

    if num_of_requests <= 0:
        return error_message_num
    try:
        response = asyncio.run(_send_all_requests(url, num_of_requests))
    except InvalidURL:
        return error_message_url
    response_message = f"Number of response: {len(response)}\n\n"
    return response_message


if __name__ == '__main__':
    url_1 = "https://mail.ru"
    url_2 = "http://httpbin.org/delay/3"

    num_of_requests = 100

    print(get_async_requests(url_1, num_of_requests))
    print(get_async_requests(url_2, num_of_requests))
