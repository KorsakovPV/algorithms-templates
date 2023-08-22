# https://contest.yandex.ru/contest/23389/problems/K/

from typing import List, Tuple


def get_sum(number_list: List[int], k: int) -> List[int]:
    j = int(''.join(map(str, number_list)))

    return [int(x) for x in str(k + j)]


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
