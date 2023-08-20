# https://contest.yandex.ru/contest/26365/problems/C/

# C. Скользящее среднее
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
#
# Измерения велись n секунд.
#
# В секунду i поступает qi запросов.
#
# Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.

from typing import List, Tuple


def moving_average(arr: List[int], window_size: int) -> List[float]:
    window_sum = sum(arr[0:window_size])
    for i in range(len(arr) - window_size + 1):

        if i != 0:
            window_sum = window_sum - arr[i - 1] + arr[i + window_size - 1]

        yield window_sum / window_size


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size


arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))
