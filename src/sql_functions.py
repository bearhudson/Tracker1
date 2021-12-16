from src.environs import *
import mysql.connector
from mysql.connector import Error


def create_server_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=mysql_host,
            user=mysql_username,
            password=mysql_pass,
            database=mysql_db,
        )
    except Error as error:
        print(f"Error: {error}")
    return connection


def run_query(connection, query):
    result = None
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as error:
        print(f"Error: {error}")


class UserConfig:

    def __init__(self, email_address):
        self.email = email_address
        self.db_con = create_server_connection()
        self.user_id = 0
        self.last_login = None
        self.gender = None
        self.age = 0
        self.weight = 0
        self.height = 0
        self.fetch_user_details()

    def fetch_user_details(self):
        get_user_details_query = f"SELECT * FROM user WHERE user_email = '{self.email}'"
        get_user_query = self.sql_select(get_user_details_query)
        print(get_user_query)
        self.user_id = get_user_query[0][0]
        self.last_login = get_user_query[0][3]
        self.gender = get_user_query[0][4]
        self.age = get_user_query[0][5]
        self.weight = get_user_query[0][6]
        self.height = get_user_query[0][7]

    def get_user_details(self):
        return self.user_id, self.email, self.last_login, self.gender, self.age, self.weight, self.height

    def sql_select(self, query):
        return run_query(self.db_con, query)

