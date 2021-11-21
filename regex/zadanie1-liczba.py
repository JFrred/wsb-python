import regex 
def numbers_only(text):
    if regex.match(r'^([\s\d]+)$', text):
        print("To jest liczba") 
    else:
        print("To nie jest liczba") 

#a = input("Podaj napis: ")
#numbers_only(a)

valid_sample = "12345"
invalid_sample = "123w456"

samples = [valid_sample, invalid_sample]
for s in samples:
    print(s)
    numbers_only(s)
