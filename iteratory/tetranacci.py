class Tetranacci:

    def __init__(self, steps):
        self.steps = steps
        self.index = 0

    def __next__(self):
        if self.index < self.steps:
            self.index += 1
            return tetranacci(self.index)

        raise StopIteration

    def __iter__(self):
        return self

# funkcja generująca kolejne liczby ciągu tetranacciego
def tetranacci(steps):
    # nieprawidłowa wartość - liczba wyrazów powinna być nie mniejsza niż 1
    if steps < 1:
        return -1

    # pierwsze 4 wyraz ciągu
    if steps < 5:
        # 3 i 4'ty wyraz ciągu są równe 1
        if steps > 3:
            return 1
        # 3 pierwsze wyrazy ciągu równe 0
        steps -= 1
        return 0
    else:
        # rekurencyjne wywołania metody tetranacci zwracające wyraz, który jest sumą 4 poprzednich wyrazów
        return tetranacci(steps - 4) + tetranacci(steps - 3) + tetranacci(steps - 2) + tetranacci(steps - 1)


input = int(input("Podaj liczbę wyrazów: "))

for a in Tetranacci(input):
    print(a, end=", ")
