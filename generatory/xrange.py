def xrange(start, end):
    while start < end:
        yield start
        start += 1


starting_point = 5
ending_point = 10

gen = xrange(starting_point, ending_point)
for i in range(ending_point - starting_point):
    print(next(gen))