class User:

    def __init__(self):
        self.user_ID = None
        self.first_name = None
        self.last_name = None
        self.password = None
        self.login_name = None

    def get_user_ID(self) -> int:
        return self.user_ID

    def get_first_name(self) -> str:
        return self.first_name

    def get_last_name(self) -> str:
        return self.last_name

    def get_password(self) -> str:
        return self.password

    def get_login_name(self) -> str:
        return self.login_name