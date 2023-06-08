import collections
import re

from hunger_games.task_f import runtime_all_methods


@runtime_all_methods
class Text:
    def __init__(self, text: str):
        self.text = text

    def get_longest_word(self) -> str:
        """Возвращает самое длинное слово в тексте."""
        try:
            longest_word = max(re.sub(r"[^А-Яа-я]", " ", self.text).split(), key=len)
        except ValueError:
            return ""
        return longest_word

    def get_most_common_word(self) -> str:
        """Возвращает самое часто встречающееся слово. Если несколько слов встречаются
        одинаковое максимальное количество раз, выводится слово, которое встречается
        в тексте первым.
        """
        words = re.sub(r"[^А-Яа-я]", " ", self.text.lower()).split()
        counter = collections.Counter(word for word in words if len(word) > 1)
        try:
            most_common, _ = counter.most_common()[0]
        except IndexError:
            return ""
        return most_common

    def get_number_of_special_characters(self) -> int:
        """Возвращает количество спецсимволов в тексте (точки, запятые и так далее)."""
        special_characters = "".join(re.sub(r"[А-Яа-я0-9]", "", self.text).split())
        number_of_special_characters = len(special_characters)
        return number_of_special_characters

    def get_all_palindromes(self) -> str:
        """Возвращает все палиндромы через запятую."""
        palindromes = []
        words = re.sub(r"[^А-Яа-я]", " ", self.text).split()
        for word in words:
            forward = "".join(word.lower())
            backward = forward[::-1]
            if forward == backward:
                palindromes.append(forward)
        palindromes = ", ".join(palindromes)
        return palindromes


if __name__ == '__main__':
    text_1 = """Написать класс, принимающий на вход текст. Один метод класса должен \
        выводить в консоль самое длинное слово в тексте. Второй метод - самое часто \
        встречающееся слово. Третий метод выводит количество спецсимволов в тексте \
        (точки, запятые и так далее). Четвертый метод выводит все палиндромы через \
        запятую."""

    text_2 = "Принимающий класс. Написать класс, принимающий на вход и текст и цифры."

    text_3 = "Дед искал довод, но заказ получил казак, поэтому устроил топот"

    # Cамое длинное слово в тексте:
    print(f"Cамое длинное слово в text_1: {Text(text_1).get_longest_word()}",
          end="\n\n")

    # Cамое часто встречающееся слово:
    print(f"Cамое часто встречающееся слово в text_2: "
          f"{Text(text_2).get_most_common_word()}", end="\n\n")

    # Количество спецсимволов в тексте:
    print(f"Количество спецсимволов в text_1: "
          f"{Text(text_1).get_number_of_special_characters()}", end="\n\n")

    # Все паллиндромы в тексте:
    print(f"Все паллиндромы в text_3: {Text(text_3).get_all_palindromes()}", end="\n\n")
