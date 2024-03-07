def filter_even_numbers(arr):
    return filter(lambda a: (a%2 == 0),arr)

arr = [6,5,4,3,2,1]

print(list(filter_even_numbers(arr)))