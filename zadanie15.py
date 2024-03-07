def add(x):
    def add2(y):
        return x + y

    return add2


addInner = add(7)

print(addInner(4))
