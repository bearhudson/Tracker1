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
        if results is None:
            print("Login Error!")
            exit(1)
        else:
            print("Login Successful.")
            self.user_id = results[0]
            self.user_string = results[2]
            self.last_login = results[4]
            self.gender = results[5]
            self.age = results[6]
            self.weight = results[7]
            self.height = results[8]

    def get_user_id(self):
        return self.user_id

    def get_user_string(self):
        return self.user_string

    def get_user_email(self):
        return self.user_email

    def get_last_login(self):
        return self.last_login

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def get_weight(self):
        return self.weight

    def get_height(self):
        return self.height

    def get_profile(self):
        return self.user_id, self.user_string, self.user_email, self.last_login, \
               self.gender, self.age, self.weight, self.height

    def user_insert_query(self, query):
        self.insert_query(query)

    def user_select_all(self, query):
        self.select_all_query(query)

    def update_last_login(self, today):
        today_str = today.strftime('%Y-%m-%d')
        query = f"UPDATE user set last_login = '{today_str}' where user_email = " \
                f"'{self.user_email}';"
        return query
