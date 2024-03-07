import functools

list_num = [1, 2, 3, 1, 21, 3]

sum_of_num = functools.reduce(lambda x, y: (x + y), list_num)

print(sum_of_num)
