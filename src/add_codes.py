import numpy as np
import xlsxwriter as xl
import pandas as pd
from datetime import date
import pprint as pp
from formats.standard_formats import *
import math

cost_rprt_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Contract Forecasting Spreadsheet\Period 2 Export 02.02.23.xlsx')
cost_rprt_df = pd.read_excel(cost_rprt_xls)

sched_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Schedule\M007 Billing Cost Schedule - 01.25.23.xlsx')
sched_df = pd.read_excel(sched_xls, sheet_name='Cost Forecast')

def array_differences(array1, array2):
    #return an array values which not shared between the two arrays
    return [x for x in array1 if x not in array2] + [x for x in array2 if x not in array1]


def add_codes_to_df(cost_report_df, schedule_df):
    missing_codes = array_differences(schedule_df['Code'].unique(), cost_report_df['Phase'].unique())
    updated_report_df = schedule_df
    for code in missing_codes:
        code_data = cost_report_df[cost_report_df['Phase'] == code]
        code_dict = {key: 0 for key in sched_df.columns}
        code_dict.update({
            'Code':code, 
            'Name': code_data['Name'].values[0],
            'Projected Forecast': code_data['Projected Cost Forecast'].sum(),
            'Spent to Date': code_data['Actual Cost'].sum(),

        })
        updated_report_df = pd.concat([updated_report_df, pd.DataFrame(code_dict, index=[0])], ignore_index=True)

    return updated_report_df.sort_values(by=['Code'])


def write_sheet(workbook, worksheet, updated_df):
    for index, col in enumerate(updated_df.columns):
        worksheet.write(0, index, col, heading_format(workbook))


    for y in range(updated_df.shape[0]):
        for x in range(updated_df.shape[1]):
            if updated_df.columns[x] == 'Final Cost':
                # CHANGE THE LETTER ON THE END OF THE SUM AS THE MONTHS CHANGE
                worksheet.write(y+1, x, f"=SUM(D{y+2}:M{y+2})", currency_format(workbook, '#FFFFFF'))
            elif updated_df.columns[x] == 'Forecast Spent %':
                # CHANGE THE LETTER ON THE NUMERATOR AS THE MONTHS CHANGE
                worksheet.write(y+1, x, f"=IF(C{y+2}=0,0,N{y+2}/C{y+2})", percent_format(workbook, '#FFFFFF'))
                # worksheet.write(y+1, x, f"=N{y+2}/C{y+2}" if updated_df.iloc[y,2] != 0 else 0, percent_format(workbook, '#FFFFFF'))
            else:
                worksheet.write(y+1, x, updated_df.iloc[y,x] if not pd.isna(updated_df.iloc[y,x]) else 0, string_format(workbook, '#FFFFFF') if (x<2 or (x>=15 and x<18)) else currency_format(workbook, '#FFFFFF'))



def create_updated_sheet(cost_report_df, schedule_df):
    updated_df = add_codes_to_df(cost_report_df, schedule_df)

    workbook = xl.Workbook('Updated Schedule.xlsx')
    worksheet = workbook.add_worksheet('Cost Forecast')
    write_sheet(workbook, worksheet, updated_df)
    workbook.close()

create_updated_sheet(cost_rprt_df, sched_df)