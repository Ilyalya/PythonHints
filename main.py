# Проверить, содержит ли список целое число x
l = [3, 3, 4, 5, 2, 111, 5]
print(111 in l)


# Найти количество дубликатов в списке целых чисел
def find_duplicates(elements):
    duplicates, seen = set(), set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    return list(duplicates)


print(find_duplicates(l))


# Проверить, являются ли две строки анаграммами
def is_anagram(s1, s2):
    return set(s1) == set(s2)


print(is_anagram("elvis", "lives"))

# Удалить все дубликаты из списка
lst = list(range(10)) + list(range(10))
lst = list(set(lst))
print(lst)


# Найдите в списке пары целых чисел, сумма которых равна целому числу x
def find_pairs(l, x):
    pairs = []
    for (i, el_1) in enumerate(l):
        for (j, el_2) in enumerate(l[i + 1:]):
            if el_1 + el_2 == x:
                pairs.append((el_1, el_2))
    return pairs


print(find_pairs(l, 7))


# Проверить, является ли строка палиндромом
def is_palindrome(phrase):
    return phrase == phrase[::-1]


print(is_palindrome("anna"))

# Использовать список как стек, массив и очередь
# Список
k = [3, 4]
k += [5, 6]
print(k)

# Стек
k.append(10)
k.pop()
print(k)

# Очередь
k.insert(0, 5)
k.pop()
print(k)


# Получить недостающее число в [1, ..., 100]
def get_missing_number(lst):
    return set(range(lst[len(lst) - 1])[1:]) - set(n)


n = list(range(1, 100))
n.remove(50)
print(get_missing_number(n))


# Вычислить пересечение двух списков
def intersect(lst1, lst2):
    res, lst2_copy = [], lst2[:]
    for el in lst1:
        if el in lst2_copy:
            res.append(el)
            lst2_copy.remove(el)
    return res


lst1 = [1, 2, 3, 4, 5, 6]
lst2 = [4, 5, 6, 7, 8, 9]
print(intersect(lst1, lst2))

# Найти максимум и минимум в отсортированном списке
v = [4, 3, 6, 3, 4, 888, 1, -11, 22, 3]
print(max(v))
print(min(l))


# Перевернуть строку с помощью рекурсии
def reverse(string):
    if len(string) <= 1: return string
    return reverse(string[1:]) + string[0]


print(reverse("hello"))

# Вычислить первые n чисел Фибоначчи
a, b = 0, 1
n = 10
for i in range(n):
    print(b)
    a, b = b, a + b


# Сортировка списка с помощью алгоритма быстрой сортировки
def qsort(L):
    if L == []: return []
    return qsort([x for x in L[1:] if x < L[0]]) + L[0:1] + qsort([x for x in L[1:] if x >= L[0]])


lst_k = [44, 33, 22, 5, 77, 55, 999]
print(qsort(lst_k))


# Найти все перестановки строки
def get_permutations(w):
    if len(w) <= 1:
        return set(w)
    smaller = get_permutations(w[1:])
    perms = set()
    for x in smaller:
        for pos in range(0, len(x)+1):
            perm = x[:pos] + w[0] + x[pos:]
            perms.add(perm)
    return perms


print(get_permutations("nan"))