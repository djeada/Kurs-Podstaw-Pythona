from timeit import Timer
from functools import lru_cache, partial


def fib_zwykly(n):
    if n <= 0:
        return 0
    return fib_zwykly(n - 1) + fib_zwykly(n - 2)


@lru_cache
def fib_memo(n):
    if n <= 0:
        return 0
    return fib_memo(n - 1) + fib_memo(n - 2)


n = 25
print(Timer(partial(fib_zwykly, n)).timeit(1))
print(Timer(partial(fib_memo, n)).timeit(1))
