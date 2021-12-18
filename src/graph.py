import matplotlib.pyplot as plt
import pandas as pd


def report(report_query, report_type):
    if report_type == 'food':
        food_report(report_query)
    elif report_type == 'exercise':
        exercise_report(report_query)


def food_report(report_query):
    labels = ['date', 'name', 'quantity', 'calories', 'weight', 'user', 'uuid']
    df = pd.DataFrame(report_query, columns=labels)
    df.set_index('date')
    plt.xlabel('Dates')
    plt.ylabel('Numbers')
    plt.title("Calories and Weight by Day")
    plt.scatter(df['date'], df['calories'], label='Calories (k)', color='purple')
    plt.scatter(df['date'], df['weight'], label='Weight (g)', color='orange')
    plt.legend()
    plt.show()
    plt.title("Food Types and Calories")
    plt.axis('equal')
    plt.pie(df['calories'], labels=df['name'])
    plt.show()


def exercise_report(report_query):
    labels = ['date', 'name', 'duration', 'calories', 'user', 'uuid']
    df = pd.DataFrame(report_query, columns=labels)
    df.set_index('date')
    plt.xlabel('Date')
    plt.ylabel('Numbers')
    plt.title("Calories by Date")
    plt.scatter(df['date'], df['calories'], label='Calories (k)', color='green')
    plt.scatter(df['date'], df['duration'], label='Weight (g)', color='red')
    plt.legend()
    plt.show()
