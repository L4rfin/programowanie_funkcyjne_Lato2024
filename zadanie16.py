def add(x):
    return x + 10


def div(x):
    return x / 3


def compose(f1, f2):
    return lambda x: f2(f1(x))


add_then_multiply = compose(add, div)
print(add_then_multiply(2))
