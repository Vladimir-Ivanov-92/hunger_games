# Hunger games

Решение тестовых заданий для участия в "Голодных играх джунов".

### В данном проекте использовались следущие инструменты:

- Python v3.11
- aiohttp v3.8
- pytest v7.3
- poetry

## Setup and run:

Для управления зависимостями через [poetry](https://python-poetry.org/):
```bash
mkdir solution_hg
cd solution_hg
git clone https://github.com/Vladimir-Ivanov-92/hunger_games.git
cd hunger_games
poetry install
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
