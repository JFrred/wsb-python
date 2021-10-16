class Chain:

    def __init__(self, *collections):
        self.index = -1
        self.merged_collections = []
        # złączenie wszystkich kolekcji w jedną
        for coll in collections:
            self.merged_collections += coll

    def __next__(self):
        # iteracja po nowo utworzonej kolekcji oraz zwrócenie każdego wyrazu po kolei
        if self.index < len(self.merged_collections) - 1:
            self.index += 1
            return self.merged_collections[self.index]

        raise StopIteration

    def __iter__(self):
        return self


collection = Chain("ABC", [1, 2, 3], [], "DEF")
for c in collection:
    print(c, end=" ")
