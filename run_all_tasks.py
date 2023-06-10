import time

from hunger_games.task_test_cases import (task_a,
                                          task_b_case_1,
                                          task_b_case_2,
                                          task_b_case_3,
                                          task_c,
                                          task_d,
                                          task_e_get_longest_word,
                                          task_e_get_most_common_word,
                                          task_e_get_number_of_special_characters,
                                          task_e_get_all_palindromes)


def main():
    tasks = [task_a, task_b_case_1, task_b_case_2, task_b_case_3, task_c,
             task_e_get_longest_word, task_e_get_most_common_word,
             task_e_get_number_of_special_characters, task_e_get_all_palindromes,
             task_d]

    for task in tasks:
        print("\n" + ("_" * 15) + f"{task.__name__}" + \
              ("_" * 15) + ":")
        print(task.__doc__)
        print("Result:")
        task()
        time.sleep(1)


if __name__ == '__main__':
    main()
