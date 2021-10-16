def repeat(element, times=None):
    # zwracanie podanego elementu w nieskończoność jeśli parametr times został pominięty
    if times is None:
        while True:
            yield element

    for i in range(times):
        yield element


for r in repeat("ahoj", 5):
    print(r, end=" ")

