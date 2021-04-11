from User import User

class CredentialDatabase:

    __json_dump_file_name = "core_user_record.json"
    credentials_login_name_to_user = {}
    credentials_uid_to_user = {}

    __instance = None

    def __init__(self):
        pass

    def get_user_from_id(self, id: int) -> User:
        pass

    def get_user_from_login_name(self, name: str) -> User:
        pass

    def add_user(self, user: User):
        pass

    @staticmethod
    def get_instance() -> CredentialDatabase:
        if CredentialDatabase.__instance == None:
            CredentialDatabase.__instance = CredentialDatabase()
        return CredentialDatabase.__instance

if __name__ == "__main__":
    pass