# Hunger games

Решение тестовых заданий для участия в "Голодных играх джунов".

### В данном проекте использовались следущие инструменты:

- Python v3.11
- aiohttp v3.8
- pytest v7.3
- poetry

## Setup and run:
Перейдите в директорию, в которую будете клонировать репозиторий.
В зависимости от того, каким менеджером зависимостей Вы пользуетесь, выполните следующие
команды:

При управлении зависимостями через [poetry](https://python-poetry.org/):
```bash
mkdir solution_hg
cd solution_hg
git clone https://github.com/Vladimir-Ivanov-92/hunger_games.git
cd hunger_games
poetry install --without dev
poetry run python3 -m pytest
poetry run python3 -m run_all_tasks
```


С помощью pip:
```bash
mkdir solution_hg
cd solution_hg
git clone https://github.com/Vladimir-Ivanov-92/hunger_games.git
cd hunger_games
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
python3 run_all_tasks.py
```

После выполнения указанных команд, будет создана папка с проектом, склонированным из 
репозитория. Запустится тестирование с помощью библиотеки pytest. После завершения
тестирования, запускается файл run_all_tasks.py и в консоль выводятся по очереди 
тестовые данные и результаты выполнения функций и методов реализующих функционал, 
указанный в заданиях. 
