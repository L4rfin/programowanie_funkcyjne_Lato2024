
def apply_twice(function1, i):
    return function1(function1(i))


print(apply_twice(lambda a: a * 2, 3))
