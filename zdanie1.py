import itertools

list1 = ["A", "B"]
list2 = ["C", "D"]
solution = list(itertools.product(list1, list2))
for e in solution:
    print(e)
