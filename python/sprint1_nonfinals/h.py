# https://contest.yandex.ru/contest/23389/problems/H/

# H. Двоичная система
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Тимофей записал два числа в двоичной системе счисления и попросил Гошу вывести их сумму, также в двоичной системе.
# Встроенную в язык программирования возможность сложения двоичных чисел применять нельзя. Помогите Гоше решить задачу.
#
# Решение должно работать за O(N), где N –— количество разрядов максимального числа на входе.
#
# Формат ввода
# Два числа в двоичной системе счисления, каждое на отдельной строке. Длина каждого числа не превосходит 10 000
# символов.
#
# Формат вывода
# Одно число в двоичной системе счисления.

from typing import Tuple
import itertools


def get_sum(first_number: str, second_number: str) -> str:
    rezult = []
    overflow = 0
    for index in range(max(len(first_number), len(second_number))):
        if len(first_number) > index and first_number[-index - 1] == "1":
            d1 = 1
        else:
            d1 = 0

        if len(second_number) > index and second_number[-index - 1] == "1":
            d2 = 1
        else:
            d2 = 0

        d = d1 + d2 + overflow

        a, b = divmod(d, 2)

        rezult.append(str(b))
        overflow = a

    if overflow:
        rezult.append(str(overflow))
    return ''.join(rezult[::-1])


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


# first_number, second_number = read_input()
# print(get_sum(first_number, second_number))
print(get_sum(first_number='1010', second_number='1011'))
