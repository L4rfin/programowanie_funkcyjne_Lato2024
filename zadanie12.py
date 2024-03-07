from functools import partial


def multi_by_3(x, y):
    return x * y


triple = partial(multi_by_3, 3)

print(triple(10))
