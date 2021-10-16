def even_generator():
    num = 0

    while True:
        yield num
        num += 2


for e in even_generator():
    print(e, end=" ")