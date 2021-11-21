import regex

def is_email_valid(text):
    pattern = "[^@]+@[^@]+\.[^@]+"
    if regex.match(pattern, text):
        print("Adres jest poprawny")
    else:
        print("Adres jest niepoprawny")

#user_input = input("Podaj email: ")
#is_email_valid(user_input)


valid_sample0 = "jan.kowalski@jakas-domena.edu"
valid_sample1 = "jan.kowalski+lista_mailingowa@jakas-domena.edu"
invalid_sample0 = "jan_kowalski"

samples = [valid_sample0, valid_sample1, invalid_sample0]
for s in samples:
    print(s)
    is_email_valid(s)
