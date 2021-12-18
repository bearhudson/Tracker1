import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


def report(report_query, report_type):
    if report_type == 'food':
        food_report(report_query)
    elif report_type == 'exercise':
        exercise_report(report_query)


def exercise_report(report_query):
    r_date = []
    r_activity = []
    r_duration = []
    r_calories = []
    for rep in report_query:
        r_date.append(rep[0])
        r_activity.append(rep[1])
        r_duration.append(rep[2])
        r_calories.append(rep[3])
    format_date = [datetime.strftime(d, '%Y/%m/%d') for d in r_date]
    x = np.array(format_date)
    y = np.array(r_calories)
    plt.xlabel('Date')
    plt.ylabel('Calories')
    plt.title("Calorie Expenditure by Day")
    plt.bar(x, y)
    plt.show()


def food_report(report_query):
    r_date = []
    r_food_name = []
    r_quantity = []
    r_calories = []
    for rep in report_query:
        r_date.append(rep[0])
        r_food_name.append(rep[1])
        r_quantity.append(rep[2])
        r_calories.append(rep[3])
    format_date = [datetime.strftime(d, '%Y/%m/%d') for d in r_date]
    x = np.array(format_date)
    y = np.array(r_calories)
    plt.xlabel('Date')
    plt.ylabel('Calories')
    plt.title("Calorie Intake by Day")
    plt.bar(x, y)
    plt.show()
