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

# print(business_days(d2, d1))


data_dic = {
    'SITE': {
            'ACTIVITIES': activities_df[activities_df['Category'] == 'SITE'],
            'BILLINGS': billing_sched_df[billing_sched_df['Category 1'] == 'SITE'],
            'COSTS': cost_sched_df[cost_sched_df['Category 1'] == 'SITE']
    },
    'NEW BUILDINGS': {
            'ACTIVITIES': activities_df[activities_df['Category'] == 'NEW BUILDINGS'],
            'BILLINGS': billing_sched_df[billing_sched_df['Category 1'] == 'NEW BUILDINGS'],
            'COSTS': cost_sched_df[cost_sched_df['Category 1'] == 'NEW BUILDINGS']
    },
    'EXISTING BUILDINGS': {
            'ACTIVITIES': activities_df[activities_df['Category'] == 'EXISTING BUILDINGS'],
            'BILLINGS': billing_sched_df[billing_sched_df['Category 1'] == 'EXISTING BUILDINGS'],
            'COSTS': cost_sched_df[cost_sched_df['Category 1'] == 'EXISTING BUILDINGS']
    }
}

# print(activities_df.columns)
# print(billing_sched_df.columns)


# pp.pprint(data_dic)

# print(cost_sched_df[])
# print(billing_sched_df['Sub'])
# print(activities_df['Sub'])
# print(billing_sched_df['Sub'].unique().tolist())
# print(activities_df['Sub'].to_list().unique())

sub_list = pd.concat([billing_sched_df['Sub'],activities_df['Sub']], axis = 0).dropna().unique().tolist()
sub_list.sort()


# pp.pprint(sub_list)
# print({sub: {} for sub in sub_list})

def create_dictionary(billing_df, activities_df, sub_list):
    dic = {sub: {} for sub in sub_list}
    for y in range(billing_df.shape[0]):
        if not pd.isna(billing_df['Category 1'][y]):
            if billing_df['Category 1'][y] in dic[billing_df['Sub'][y]]:
                if billing_df['SOV Level 1'][y] not in dic[billing_df['Sub'][y]][billing_df['Category 1'][y]]:
                    dic[billing_df['Sub'][y]][billing_df['Category 1'][y]][billing_df['SOV Level 1'][y]] = None
            else:
                dic[billing_df['Sub'][y]][billing_df['Category 1'][y]] = {}
                dic[billing_df['Sub'][y]][billing_df['Category 1'][y]][billing_df['SOV Level 1'][y]] = None


    for y in range(activities_df.shape[0]):
        if not pd.isna(activities_df['Category'][y]):
            if activities_df['Category'][y] in dic[activities_df['Sub'][y]]:
                if activities_df['Area'][y] not in dic[activities_df['Sub'][y]][activities_df['Category'][y]]:
                    dic[activities_df['Sub'][y]][activities_df['Category'][y]][activities_df['Area'][y]] = None
            else:
                dic[activities_df['Sub'][y]][activities_df['Category'][y]] = {}
                dic[activities_df['Sub'][y]][activities_df['Category'][y]][activities_df['Area'][y]] = None

    return dic

# pp.pprint(create_dictionary(billing_sched_df, activities_df, sub_list))


workbook = xl.Workbook('Comparison.xlsx')
worksheet = workbook.add_worksheet('Comparison Summary')

# write headings

worksheet.write(0,0, 'Subcontractor', heading_format(workbook))
worksheet.write(0,1, 'Category', heading_format(workbook))
worksheet.write(0,2, 'Building', heading_format(workbook))
worksheet.write(0,3, 'Type', heading_format(workbook))
worksheet.write(0,4, 'February', heading_format(workbook))
worksheet.write(0,5, 'March', heading_format(workbook))
worksheet.write(0,6, 'April', heading_format(workbook))
worksheet.write(0,7, 'May', heading_format(workbook))
worksheet.write(0,8, 'June', heading_format(workbook))
worksheet.write(0,9, 'July', heading_format(workbook))
worksheet.write(0,10, 'August', heading_format(workbook))
worksheet.write(0,11, 'September', heading_format(workbook))
worksheet.write(0,12, 'October', heading_format(workbook))

# write data
dic = create_dictionary(billing_sched_df, activities_df, sub_list)
row = 1
for subcontractor in dic:
    worksheet.write(row, 0, subcontractor)
    row += 1
    for category in dic[subcontractor]:
        worksheet.write(row, 1, category)
        row += 1
        for area in dic[subcontractor][category]:
            worksheet.write(row, 2, area)
            worksheet.write(row, 3, 'Billings')
            worksheet.write(row+1, 3, 'Costs')
            worksheet.write(row+2, 3, 'Activities')
            row += 3
            


workbook.close()