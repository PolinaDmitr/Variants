from functools import lru_cache


@lru_cache(None)
def f(x):
    if x <= 2: return 5
    return f(x - 2) + x


for i in range(23023):
    f(i)
print(f(23023))