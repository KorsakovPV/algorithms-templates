# https://contest.yandex.ru/contest/26365/problems/B/

# B. Застёжка-молния
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Даны два массива чисел длины n. Составьте из них один массив длины 2n, в котором числа из входных массивов
# чередуются (первый — второй — первый — второй — ...). При этом относительный порядок следования чисел из одного
# массива должен быть сохранён.

from typing import List, Tuple


def zipper(a: List[int], b: List[int]) -> List[int]:
    for i in range(len(a)):
        yield a[i]
        yield b[i]


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
print(" ".join(map(str, zipper(a, b))))
