from datetime import date
import pandas as pd
from datetime import date, timedelta as td, datetime as dt



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

def last_day_of_month(any_day):
    """Return the last day of the month for the given date"""
    next_month = any_day.replace(day=28) + td(days=4)  # this will never fail
    return next_month - td(days=next_month.day)

def days_in_month(month, start_date, end_date):
    '''return the number of days between start date and end date that fall in the month'''
    days_1 = 0 if start_date.month != month else start_date.day
    days_2 = last_day_of_month(end_date) if end_date.month != month else end_date.day
    
    return  pd.Timestamp(days_2) - pd.Timestamp(days_1)