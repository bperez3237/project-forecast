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
cost_sched_df = pd.read_excel(sched_xls, sheet_name='Cost Forecast')


spent_codes = []
overspent_codes = []
for y in range(cost_sched_df.shape[0]):
    # initial value is new spent
    spent = cost_rprt_df[cost_rprt_df['Phase'] == cost_sched_df['Code'][y]]['Actual Cost'].sum() - cost_sched_df['Spent to Date'][y]
    if spent != 0 and abs(spent) > 0.01:
        if spent < cost_sched_df['January'][y]:
            spent_codes.append({cost_sched_df['Code'][y] : spent})
            cost_sched_df.iloc[y, 4] -= spent
            cost_sched_df.iloc[y, 3] = cost_rprt_df[cost_rprt_df['Phase'] == cost_sched_df['Code'][y]]['Actual Cost'].sum()
        else:
            overspent_codes.append({cost_sched_df['Code'][y] : spent})



pp.pprint(spent_codes)
pp.pprint(overspent_codes)
print(cost_sched_df[cost_sched_df['Code'] == '00-0024'])

# write updated cost schedule to excel sheet
