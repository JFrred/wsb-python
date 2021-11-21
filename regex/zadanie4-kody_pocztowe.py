import regex

def is_postal_code(text):
    pattern = "([0-9]{2})-([0-9]{3})"
    if regex.match(pattern, text):
        print("Kod jest poprawny")
    else:
        print("Kod jest niepoprawny")

#user_input = input("Podaj kod: ")
#is_postal_code(user_input)

valid_sample0 = "12-345"
valid_sample1 = "98-765"
invalid_sample0 = "ab-cde"
invalid_sample1 = "123-45"

samples = [valid_sample0, valid_sample1, invalid_sample0, invalid_sample1]
for s in samples:
    print(s)
    is_postal_code(s)