# https://contest.yandex.ru/contest/23389/problems/F/
import string


# F. Палиндром
# Ограничение времени	1 секунда
# Ограничение памяти	64Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Помогите Васе понять, будет ли фраза палиндромом‎. Учитываются только буквы и цифры, заглавные и строчные буквы
# считаются одинаковыми.
#
# Решение должно работать за O(N), где N — длина строки на входе.
#
# Формат ввода
# В единственной строке записана фраза или слово. Буквы могут быть только латинские. Длина текста не превосходит 20000
# символов.
#
# Фраза может состоять из строчных и прописных латинских букв, цифр, знаков препинания.
#
# Формат вывода
# Выведите «True», если фраза является палиндромом, и «False», если не является.

def is_palindrome(line: str) -> bool:
    l = 0
    p = len(line) - 1

    while l < p:

        while line[l] not in string.ascii_letters + string.digits and l < p:
            l += 1

        while line[p] not in string.ascii_letters + string.digits and l < p:
            p -= 1

        if line[l].lower() != line[p].lower():
            return False
        l += 1
        p -= 1
    return True


print(is_palindrome(input().strip()))
