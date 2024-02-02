from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 10:
        return n
    return g(f(n - 1) % 10) + f(g(n % 10) - 1) - f(n - 3)


@lru_cache(None)
def g(n):
    if n < 10:
        return -n
    return f(g(n - 1) % 10) + g(f(n - 1) - 1) + g(n - 2)


for i in range(1110):
    f(i)
    g(i)

print(f(1111) + g(1111))


