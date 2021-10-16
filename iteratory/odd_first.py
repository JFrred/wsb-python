class OddFirst:

    def __init__(self, args):
        self.list = args
        self.index = -1

    def __next__(self):
        # układanie w liście co drugiego elemntu zaczynając od indeksu = 0 dla nieparzystych elementów,
        # a potem od indeksu = 1 dla parzystych
        odds_evens = self.list[::2] + self.list[1::2]
        if self.index < len(odds_evens) - 1:
            self.index += 1
            return odds_evens[self.index]

        raise StopIteration

    def __iter__(self):
        return self


for o in OddFirst(["A", "B", "C", "D", "E"]):
    print(o, end=" ")

