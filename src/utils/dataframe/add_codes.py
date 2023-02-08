import numpy as np
import xlsxwriter as xl
import pandas as pd
from datetime import date
import pprint as pp
import math
from .dataframe_utils import array_differences

cost_rprt_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Contract Forecasting Spreadsheet\Period 2 Export 02.02.23.xlsx')
cost_rprt_df = pd.read_excel(cost_rprt_xls)

sched_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Schedule\M007 Billing Cost Schedule - 01.25.23.xlsx')
sched_df = pd.read_excel(sched_xls, sheet_name='Cost Forecast')


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

