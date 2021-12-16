from src.environs import *
from src.sql_functions import *


class SheetsUpdater(UserConfig):

    def __init__(self, email_address, row_type):
        super().__init__(email_address)
        self.row_type = row_type
        record_count_query = f"SELECT COUNT(*) from {self.row_type} where {self.row_type}.user = {self.user_id}"
        self.record_count = self.sql_select(record_count_query)
        if self.record_count == 0:
            print("No records found!")
            print(f"Type {self.row_type}")
        else:
            print("Records found!")
            print(f"Type {self.row_type}")

    def get_rows(self):
        self.sql_select()

    def set_row(self):
        pass

    def edit_row(self):
        pass

    def delete_row(self):
        pass
