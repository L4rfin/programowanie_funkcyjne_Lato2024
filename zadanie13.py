def calculate_factorial(x):
    if x == 1:
        return 1
    if x > 1:
        return x * calculate_factorial(x - 1)

    return 0


print(calculate_factorial(3))
