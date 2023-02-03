from numpy import number
import xlsxwriter as xl
import pandas as pd
from datetime import date
import pprint as pp
from formats import *

cost_rprt_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Contract Forecasting Spreadsheet\Period 2 Export 02.02.23.xlsx')
cost_rprt_df = pd.read_excel(cost_rprt_xls)

sched_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Schedule\M007 Billing Cost Schedule - 01.25.23.xlsx')
sched_df = pd.read_excel(sched_xls, sheet_name='Cost Forecast')

# print(cost_rprt_df.columns)
# print(sched_df.columns)

def add_codes(cost_report_df, schedule_df):
    updated_report_df = cost_report_df
    # for code in cost_report_df:
    #     pass


    return updated_report_df


