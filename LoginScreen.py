from LoginOpEnum import LoginOpEnum

class LoginScreen:

    def __init__(self):
        pass

    def display_login_form(self):
        print("Welcome to login interface!")

    def get_decision(self) -> LoginOpEnum:
        choice = input("Please choose your operation [LOGIN/REGISTER]: ")
        if choice == "LOGIN":
            return LoginOpEnum.LOGIN
        if choice == "REGISTER":
            return LoginOpEnum.REGISTER
        print("Did not recognize your choice, please try again")
        return self.get_decision()

    def get_login_name_input(self) -> str:
        return input("USER NAME:")

    def get_password_input(self) -> str:
        return input("PASSWORD:")

    def failure(self):
        print("Login failed!")