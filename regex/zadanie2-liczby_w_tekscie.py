import regex

def find_numbers(text):
    return regex.findall("[0-9]+", text)

#user_input = input("Podaj napis: ")
#result = find_numbers(user_input)

sample_text = "Alicja ma 2 koty i 3 psy"
result = find_numbers(sample_text)
print("Zanlezione liczby: ", result) 