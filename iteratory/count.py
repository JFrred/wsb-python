class Counter:
    def __init__(self, starting_point, step, n):
        self.step = step
        self.start = starting_point
        self.end = starting_point + n

    def __next__(self):
        if self.start < self.end:
            self.start += self.step
            return self.start

        raise StopIteration

    def __iter__(self):
        return self


counter = Counter(0, 1, 10)
for i in counter:
    print(i, end=", ")