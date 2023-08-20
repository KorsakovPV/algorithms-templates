# https://contest.yandex.ru/contest/26365/problems/D/

# D. Две фишки
# Ограничение времени	4 секунды
# Ограничение памяти	256Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков. Сначала Гоша
# называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.
#
# Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи.
# Помогите ей написать программу для поиска нужных фишек.

from typing import List, Tuple, Optional


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    helper = set()
    for a in arr:
        helper.add(a)
        if target_sum - a in helper:
            return target_sum - a, a

    return None

# def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             sum = arr[i] + arr[j]
#             if target_sum == sum:
#                 return arr[i], arr[j]
#     return None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))
