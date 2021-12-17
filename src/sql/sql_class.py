import mysql.connector
from mysql.connector import Error
from src.environs import *


class SQLClass:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host=mysql_host,
                user=mysql_username,
                password=mysql_pass,
                database=mysql_db,
            )
            print("Connect successful")
        except Error as error:
            print(f"Error: {error}")

    def select_all_query(self, query):
        success = False
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
        except Error as err:
            print(f"Error: '{err}'")
        return results

    def select_one_query(self, query):
        success = False
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchone()
        except Error as err:
            print(f"Error: '{err}'")
        return results