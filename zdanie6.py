def safe_function(fun):
    def wrapper(*args, **kwargs):
        try:
            return fun(*args,**kwargs)
        except Exception as e:
            print(e)
            return None
    return wrapper
@safe_function
def dziel(a, b):
    return a / b

print(dziel(10, 2))
print(dziel(10, 0))