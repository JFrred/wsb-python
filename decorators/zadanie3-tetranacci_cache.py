from functools import cache

@cache
def tetranacci_cache(n):
    if n <= 0:
        return -1
    if n <= 3:
        return 0
    if n <= 5:
        return 1
    else:
        return tetranacci_cache(n - 4) + tetranacci_cache(n - 3) + tetranacci_cache(n - 2) + tetranacci_cache(n - 1)

print(tetranacci_cache(10))