# https://contest.yandex.ru/contest/23389/problems/C/

# C. Соседи
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей. Соседним считается элемент,
# находящийся от текущего на одну ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.
#
# Например, в матрице A соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.
#
#
#
# Формат ввода
# В первой строке задано n — количество строк матрицы. Во второй — количество столбцов m. Числа m и n не превосходят
# 1000. В следующих n строках задана матрица. Элементы матрицы — целые числа, по модулю не превосходящие 1000.
# В последних двух строках записаны координаты элемента, соседей которого нужно найти. Индексация начинается с нуля.

from typing import List, Tuple

neighbor_coords = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
)


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    neighbors: List[int] = []

    for neighbor_coord in neighbor_coords:
        neighbor_row = row + neighbor_coord[0]
        neighbor_col = col + neighbor_coord[1]
        if 0 <= neighbor_row < len(matrix) and 0 <= neighbor_col < len(matrix[0]):
            neighbors.append(matrix[neighbor_row][neighbor_col])

    neighbors.sort()
    return neighbors


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
