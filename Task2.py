# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

i = 0
my_list = []

result_list = list(input('Введите несколько целых чисел через пробел: '))
result_list.append(my_list)
i += 1

print(my_list)

#
#
# result_list.insert(0, 1)
# print(result_list)
# result_list.insert(2, 3)
# print(result_list)
# result_list.insert(4, 5)
# my_list = list(input('Введите несколько целых чисел через пробел: '))
i = 0
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
    i += 1

# my_list = list(input('Введите несколько целых чисел через пробел: '))
