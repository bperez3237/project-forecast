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

def last_day_of_month(month, year):
    """Return the last day of the month"""
    if month == 12:
        return date(year, month, 31)
    else:
        return date(year, month + 1, 1) - td(days=1)
    
    

def days_in_month(month, start_date, end_date):
    '''return the number of days between start date and end date that fall in the month'''
    start_month = start_date.month
    end_month = end_date.month
    
    # if start_date > end_date:
    #     start_date, end_date = end_date, start_date
    
    
    if month < start_month or month > end_month:
        return 0
    
    elif month == start_month and month == end_month:
        return (end_date - start_date).total_seconds() / 86400
    
    elif month == start_month and month != end_month:
        return (last_day_of_month(month, start_date.year) - dt.fromtimestamp(start_date.timestamp()).date()).total_seconds() / 86400
    
    elif month != start_month and month == end_month:
        return int(end_date.strftime('%d'))
    
    elif month != start_month and month != end_month:
        return last_day_of_month(month, start_date.year).day
    

'''
strt1 = pd.Timestamp('2019-02-01')
end1 = pd.Timestamp('2019-02-23')

strt2 = pd.Timestamp('2019-01-13')
end2 = pd.Timestamp('2019-02-03')


strt3 = pd.Timestamp('2019-01-11')
end3 = pd.Timestamp('2019-03-23')


strt4 = pd.Timestamp('2019-01-21')
end4 = pd.Timestamp('2019-03-23')

strt5 = pd.Timestamp('2019-01-19')
end5 = pd.Timestamp('2019-03-23')

print('## case 1')
print(days_in_month(1, strt1, end1), f"should equal 0")
print(days_in_month(3, strt1, end1), f"should equal 0")
print('## case 2')
print(days_in_month(2, strt1, end1), f"should equal 22")
print(days_in_month(1, strt3, strt4), f"should equal 10")
print("## case 3")
print(days_in_month(2, end2, end3), "should equal 26")
print("## case 4")
print(days_in_month(3, strt4, end4), 'should equal 23')
print("## case 5")
print(days_in_month(2, strt5, end5), 'should equal 28')
'''
