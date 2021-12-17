import mysql.connector.errors
from src.environs import *
from src.sql.sql_class import SQLClass


class UserClass(SQLClass):
    def __init__(self, email):
        super().__init__()
        self.user_email = email
        self.user_id = ""
        self.last_login = ""
        self.user_string = ""
        self.gender = ""
        self.age = 0
        self.weight = 0
        self.height = 0

    def check_login(self):
        query = f"SELECT * from user where user_email = '{self.user_email}';"
        results = self.select_one_query(query)
        self.user_id = results[0]
        self.user_string = results[2]
        self.last_login = results[4]
        self.gender = results[5]
        self.age = results[6]
        self.weight = results[7]
        self.height = results[8]

    def get_profile(self):
        return self.user_id, self.user_string, self.user_email, self.last_login
