valid_login = "u"
valid_password = "1"

class NotLoggedIn(Exception):
    def __init__(self, message="Wrong credentials"):
        self.message = message
        super().__init__(self.message)

def login_required(func):
    def inner(a, b):
        login = input("login: ")
        password = input("password: ")

        if (login == valid_login and password == valid_password):
            return func(a, b) 
        else:
            raise NotLoggedIn

    return inner


@login_required
def add_two_numbers_secured(a, b):
    print(a + b)
    
    
add_two_numbers_secured(10, 90)
