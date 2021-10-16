def accumulate(collection):
    current_item = ""
    # index = -1

    for arg in collection:
        current_item += str(arg)
        yield current_item


gen = accumulate(['ala ', 'ma', ' kota'])
print(next(gen))
print(next(gen))
print(next(gen))



