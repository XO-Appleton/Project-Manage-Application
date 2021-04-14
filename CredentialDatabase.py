from __future__ import annotations
import json
from os.path import *

from User import User

class CredentialDatabase:

    __json_dump_file_name = "core_user_record.json"
    # credentials_login_name_to_user = {}
    # credentials_uid_to_user = {}
    __user_records: list = None
    __user_count = None

    __instance = None

    def __init__(self):
        self.load_database()

    def get_user_from_id(self, id: int) -> User:
        for u in self.__user_records:
            if u.get_user_ID() == id:
                return u

    def get_user_from_login_name(self, name: str) -> User:
        for u in self.__user_records:
            if u.get_login_name() == name:
                return u

    def add_user(self, user: User):
        user.user_ID = self.__user_count
        self.__user_count += 1
        self.__user_records.append(user)
        self.save_database()

    def load_database(self):
        self.__user_records = []
        if not isfile(self.__json_dump_file_name):
            with open(self.__json_dump_file_name, "w") as fp:
                json.dump({"user_count": 0, "records": []}, fp)
        
        with open(self.__json_dump_file_name) as fp:
            raw = json.load(fp)
        self.__user_count = raw["user_count"]
        user_records = raw["records"]
        for record in user_records:
            u = User()
            u.user_ID = record["user_ID"]
            u.first_name = record["first_name"]
            u.last_name = record["last_name"]
            u.login_name = record["login_name"]
            u.password = record["password"]
            self.__user_records.append(u)

    def save_database(self):
        with open(self.__json_dump_file_name, "w") as fp:
            json.dump({"user_count": self.__user_count, "records": [u.__dict__ for u in self.__user_records]}, fp)

    @staticmethod
    def get_dump_file_name():
        return CredentialDatabase.__json_dump_file_name

    @staticmethod
    def get_instance() -> CredentialDatabase:
        if CredentialDatabase.__instance == None:
            CredentialDatabase.__instance = CredentialDatabase()
        return CredentialDatabase.__instance

if __name__ == "__main__":
    import os
    if os.path.isfile(CredentialDatabase.get_dump_file_name()):
        os.remove(CredentialDatabase.get_dump_file_name())
    db = CredentialDatabase.get_instance()

    u = User()
    u.first_name = "Lennon"
    u.last_name = "Yu"
    u.password = "foo"
    u.login_name = "yun12"
    db.add_user(u)

    u = User()
    u.first_name = "Davlid"
    u.last_name = "Lai"
    u.password = "bar"
    u.login_name = "laid3"
    db.add_user(u)

    print(db.get_user_from_login_name("laid3").get_first_name())
    u = User()
    u.first_name = "Dennis"
    u.last_name = "Liao"
    u.password = "foobar"
    u.login_name = "liaod"
    db.add_user(u)
    db.save_database()