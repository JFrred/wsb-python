def hello(func):
    def inner(a, b):
        print("hello")
    
        print(func(a, b))

    return inner


@hello
def add_two_numbers(a, b):
    return a + b 


add_two_numbers(1, 2)
add_two_numbers(5, 5)
