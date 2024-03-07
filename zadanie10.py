def even_number_generator():
    x = 0
    while True:
        yield x
        x += 2


gen = even_number_generator()

first_5 = [next(gen) for _ in range(10)]
print(first_5)