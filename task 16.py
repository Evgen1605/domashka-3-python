# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint

n = int(input('количество элементов в массиве: '))
nums = list(map(int, input('Введите список через пробел: ').split(' ')))
x = int(input('Введите число X: '))

count = 0
for i in range(n):
    if nums[i] == x:
        count += 1

print(f'Число {x} встречается в списке А {count} раз.')

result = [i for i in range(n) if nums[i] == x]
print(f'Число {x} встречается в списке А {len(result)} раз.')


# решение преподавателя 
len_nums = int(input('Enter list length: '))
nums = [randint(1, 100) for i in range(len_nums)]
print("List: ", *nums)
x = int(input('Enter x: '))

# easy
print(f'{x} finds in list {nums.count(x)} times')

# hard
print(f'{x} finds in list {len([i for i in nums if i == x])} times')
