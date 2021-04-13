from LoginScreen import LoginScreen
from RegistrationScreen import RegistrationScreen
from LoginOpEnum import LoginOpEnum
from CredentialDatabase import CredentialDatabase

class LoginCoordinator:

    def start_login_process(self):
        login = LoginScreen()
        login.display_login_form()
        decision = login.get_decision()

        if decision == LoginOpEnum.LOGIN:
            while True:
                username = login.get_login_name_input()
                password = login.get_password_input()
                user = self.validate(username, password)
                if user is None:
                    login.failure()
                    continue
                print("Login successful.")
                return user

        elif decision == LoginOpEnum.REGISTER:
            while True:
                register = RegistrationScreen()
                register.display_registration_form()
                new_user = register.get_input()
                if self.validate_new_user(new_user):
                    return new_user

            
    def validate(self, username, password):
        db = CredentialDatabase().get_instance()
        user = db.get_user_from_login_name(username)
        if user and user.password == password:
            return user
        else:
            return None

    def validate_new_user(self, new_user):
        db = CredentialDatabase().get_instance()
        if db.get_user_from_login_name(new_user.login_name):
            print("Registration failure, user already exissts.")
            return False
        else:
            db.add_user(new_user)
            print("User added.")
            return True

if __name__ == "__main__":
    test = LoginCoordinator()
    test.start_login_process()
