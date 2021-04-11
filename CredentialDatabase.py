from User import User

class CredentialDatabase:

    credentials_login_name_to_user = {}
    credentials_uid_to_user = {}

    def get_user_from_id(self, id: int) -> User:
        pass

    def get_user_from_login_name(self, name: str) -> User:
        pass

    def add_user(self, user: User):
        pass