from food_processor import input_food
from exercise_machine import input_exercise
from sheets_updater import SheetsUpdater
from environs import *

# food_input = input_food()
food_sheet = SheetsUpdater(food_sheet_name)
workout_input = input_exercise()
workout_sheet = SheetsUpdater(workout_sheet_name)

for index in workout_input:
    workout_sheet.add_row(entry_type='workout', add_object=index)
print(workout_sheet.get_sheets())
print(food_sheet.get_sheets())
