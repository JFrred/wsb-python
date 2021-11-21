# funkcja zwracające n-ty wyraz ciągu teranacciego
def tetranacci(n):
    if n <= 0:
        return -1
    if n <= 3:
        return 0
    if n <= 5:
        return 1
    else:
        # rekurencyjne wywołania metody tetranacci zwracające wyraz, który jest sumą 4 poprzednich wyrazów
        return tetranacci(n - 4) + tetranacci(n - 3) + tetranacci(n - 2) + tetranacci(n - 1)

print(tetranacci(10))
