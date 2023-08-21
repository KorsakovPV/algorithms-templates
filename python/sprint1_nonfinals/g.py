# https://contest.yandex.ru/contest/23389/problems/G/

# G. Работа из дома
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Вася реализовал функцию, которая переводит целое число из десятичной системы в двоичную. Но, кажется, она получилась
# не очень оптимальной.
#
# Попробуйте написать более эффективную программу.
#
# Не используйте встроенные средства языка по переводу чисел в бинарное представление.

def to_binary(number: int) -> str:
    if number == 0:
        return 0
    a, b = divmod(number, 2)
    if a > 1:
        return f'{to_binary(a)}{b}'
    else:
        return f'{a}{b}'


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
