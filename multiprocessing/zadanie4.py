import multiprocessing 

def power(num):
    return num*num

#pobierz liczby od użytkownika i zapisz je w liście
numbers = []
for i in range(3):
    u_input = int(input())
    numbers.append(u_input)

#obliczanie potęg liczb podanych przez użytkownika za pomocą funkcji map
result = multiprocessing.Pool().map(power, numbers)

print(result)

