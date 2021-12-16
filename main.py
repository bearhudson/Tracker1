from src.food_processor import *
from src.sheets_updater import *

# workout_input = input_exercise()
# workout_sheet = SheetsUpdater(workout_sheet_name)
#
# for index in workout_input:
#     workout_sheet.add_row(entry_type='workout', add_object=index)
# print(workout_sheet.get_sheets())
#
# print(food_sheet.get_sheets())

tracker_user = input("Which user? ")
tracker_user = UserConfig(tracker_user)
tracker_user.fetch_user_details()
print(tracker_user.get_user_details())
exercise_sheet = SheetsUpdater(tracker_user, row_type='exercise')
