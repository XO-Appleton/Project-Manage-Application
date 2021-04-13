from User import User

class RegistrationScreen:

    def display_registration_form(self):
        print("Welcome to new user registration interface")

    def get_input(self) -> User:
        new_user = User()
        new_user.first_name = input("FIRST NAME:")
        new_user.last_name = input("LAST NAME:")
        new_user.login_name = input("LOGIN NAME:")
        new_user.password = input("PASSWORD:")
        return new_user


if __name__ == "__main__":
    print(RegistrationScreen().get_input().login_name)