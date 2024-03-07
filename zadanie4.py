import time


def timeis(func):
    def wrap(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(func.__name__, end - start)
        return result

    return wrap


@timeis
def f1():
    time.sleep(2)

f1()