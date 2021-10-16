class Repeat:

    def __init__(self, elem, times):
        self.elem = elem
        self.index = 0
        self.times = times

    def __next__(self):
        # zwracanie elementu w nieskończoność jeśli parametr times = 0 lub został pominięty
        if self.times == "0" or self.times == "":
            return self.elem

        if self.index < int(self.times):
            self.index += 1
            return self.elem
        else:
            raise StopIteration

    def __iter__(self):
        return self


element = input("Podaj element: ")
n = input("Podaj liczbę: ")

for r in Repeat(element, n):
    print(r, end=" ")
