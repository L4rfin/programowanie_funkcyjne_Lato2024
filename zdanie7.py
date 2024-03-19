from itertools import groupby

liczby = [1,2,3,4,5,6,7,8,9]
zgrupowane_liczby = {k: list(v) for k, v in groupby(liczby, key=lambda x:x%2)}
print(zgrupowane_liczby)