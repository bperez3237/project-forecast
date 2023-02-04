from datetime import date
import pandas as pd



def business_days(day_1, day_2):
    """Return the number of business days between two dates"""
    # If day_1 is later than day_2, switch them
    if day_1 > day_2:
        day_1, day_2 = day_2, day_1

    # Count the number of days from day_1 to day_2
    days = (day_2 - day_1).days + 1

    # Count the number of weekends between day_1 and day_2
    weekends = days // 7 * 2

    # If day_2 is a Saturday, then there is one more weekend
    if day_2.weekday() == 5:
        weekends += 1

    # If day_1 is a Sunday, then there is one more weekend
    if day_1.weekday() == 6:
        weekends += 1

    # Return the number of business days
    return days - weekends