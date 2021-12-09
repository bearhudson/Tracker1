from food_processor import input_food
from exercise_machine import input_exercise
from sheets_updater import SheetsUpdater
from environs import *

# input_exercise()
# input_food()

workout_sheet = SheetsUpdater(workout_sheet_name)
print(workout_sheet.get_sheets())

food_sheet = SheetsUpdater(food_sheet_name)
print(food_sheet.get_sheets())
