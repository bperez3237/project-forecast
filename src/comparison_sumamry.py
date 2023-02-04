import numpy as np
import xlsxwriter as xl
import pandas as pd
from datetime import date
import pprint as pp
from formats.standard_formats import *
import math

cost_rprt_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Contract Forecasting Spreadsheet\Period 2 Export 02.02.23.xlsx')
cost_rprt_df = pd.read_excel(cost_rprt_xls)

sched_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Schedule\M007 Billing Cost Schedule - 02.03.23.xlsx')
cost_sched_df = pd.read_excel(sched_xls, sheet_name='Cost Forecast')

billing_sched_df = pd.read_excel(sched_xls, sheet_name='Billing Forecast')

activities_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\27 - PERSONAL FOLDERS\Brian Perez\Coney Island\03 - Schedule\All Activities January 2023.xlsx')
activities_df = pd.read_excel(activities_xls, sheet_name='TASK')


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

d1 =  date(2023, 2,6)
d2 = date(2023, 1,31)

print(business_days(d2, d1))



data_dic = {
    'SITE': {
            'ACTIVITIES': activities_df[activities_df['Category'] == 'SITE'],
            'BILLINGS': billing_sched_df[billing_sched_df['Category 1'] == 'SITE'],
            'COSTS': cost_rprt_df[cost_rprt_df['Category 1'] == 'SITE']
    },
    'NEW BUILDINGS': {
            'ACTIVITIES': activities_df[activities_df['Category'] == 'NEW BUILDINGS'],
            'BILLINGS': billing_sched_df[billing_sched_df['Category 1'] == 'NEW BUILDINGS'],
            'COSTS': cost_rprt_df[cost_rprt_df['Category 1'] == 'NEW BUILDINGS']
    },
    'EXISTING BUILDINGS': {
            'ACTIVITIES': activities_df[activities_df['Category'] == 'EXISTING BUILDINGS'],
            'BILLINGS': billing_sched_df[billing_sched_df['Category 1'] == 'EXISTING BUILDINGS'],
            'COSTS': cost_rprt_df[cost_rprt_df['Category 1'] == 'EXISTING BUILDINGS']
    }
}