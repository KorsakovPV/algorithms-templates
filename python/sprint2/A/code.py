# https://contest.yandex.ru/contest/23758/problems/?nc=apJxCqaT

# A. Мониторинг
# Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
# Все языки	1 секунда	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
# Node.js 14.15.5	1 секунда	128Mb
# Oracle Java 8	4 секунды	150Mb
# OpenJDK Java 11	4 секунды	150Mb
# C# (MS .NET 6.0 + ASP)	4 секунды	150Mb
# Kotlin 1.8.0 (JRE 11)	4 секунды	150Mb
# C# (MS .NET 5.0 + ASP)	4 секунды	150Mb
# Node JS 8.16	1 секунда	128Mb
# Алла получила задание, связанное с мониторингом работы различных серверов. Требуется понять, сколько времени
# обрабатываются определённые запросы на конкретных серверах. Эту информацию нужно хранить в матрице, где номер
# столбца соответствуют идентификатору запроса, а номер строки — идентификатору сервера. Алла перепутала строки и
# столбцы местами. С каждым бывает. Помогите ей исправить баг.
#
# Есть матрица размера m × n. Нужно написать функцию, которая её транспонирует.
#
# Транспонированная матрица получается из исходной заменой строк на столбцы.
#
# Например, для матрицы А (слева) транспонированной будет следующая матрица (справа):


def get_transp_arr(m, n, arr):
    return zip(*arr)


def read_input():
    m = input().strip()
    n = input().strip()
    arr = []
    for _ in range(int(m)):
        arr.append(input().strip().split())
    # m = int('4'.strip())
    # n = int('3'.strip())
    # arr = []
    # arr.append(list('1 2 3'.strip().split()))
    # arr.append(list('0 2 6'.strip().split()))
    # arr.append(list('7 4 1'.strip().split()))
    # arr.append(list('2 7 0'.strip().split()))
    return m, n, arr


m, n, arr = read_input()
for line in get_transp_arr(m, n, arr):
    print(' '.join(line))
