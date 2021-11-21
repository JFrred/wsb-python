import regex

def is_hex_color(text):
    pattern = "^#(?:[0-9a-fA-F]{3}){1,2}$"
    if regex.match(pattern, text):
        print("Zapis poprawny")
    else:
        print("Zapis niepoprawny")

#user_input = input("Podaj napis: ")
#is_hex_color(user_input)

valid_sample0 = "#FFFFFF"
valid_sample1 = "#FAF"
invalid_sample0 = "#FEAF"
invalid_sample1 = "#XXX"
samples = [valid_sample0, valid_sample1, invalid_sample0, invalid_sample1]

for s in samples:
    print(s) 
    is_hex_color(s)
