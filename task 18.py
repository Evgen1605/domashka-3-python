# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример: *

# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

n = int(input('количество элементов в массиве: '))
nums = list(map(int, input('Введите список через пробел: ').split(' ')))
x = int(input('Введите число X: '))

min = abs(x - nums[0])
index = 0
for i in range(1, n):
    count = abs(x - nums[i])
    if count < min:
        min = count
        index = i
print(
    f'Число X: {x} в списке A, наиболее близко по величине к числу {nums[index]}')


# решение преподавателя
len_nums = int(input('Enter list length: '))
nums = [randint(1, 100) for i in range(len_nums)]
print("List: ", *nums)
x = int(input('Enter x: '))

# easy
min_diff = nums[0]
for i in nums:
    diff_current = abs(i-x)
    if diff_current < min_diff:
        res = i
min_diff = diff_current

res = min([i for i in nums if abs(i-x) == min_diff])
print(f'Result is {res}')

# pro
print(f'Result is {min(nums, key=lambda y: abs(y-x))}')
