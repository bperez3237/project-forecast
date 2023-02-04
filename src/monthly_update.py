import numpy as np
import xlsxwriter as xl
import pandas as pd
from datetime import date
import pprint as pp
from formats import *
import math

cost_rprt_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Contract Forecasting Spreadsheet\Period 2 Export 02.02.23.xlsx')
cost_rprt_df = pd.read_excel(cost_rprt_xls)

sched_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Schedule\M007 Billing Cost Schedule - 02.03.23.xlsx')
cost_sched_df = pd.read_excel(sched_xls, sheet_name='Cost Forecast')

billing_sched_df = pd.read_excel(sched_xls, sheet_name='Billing Forecast')

activities_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\27 - PERSONAL FOLDERS\Brian Perez\Coney Island\03 - Schedule\All Activities January 2023.xlsx')
activities_df = pd.read_excel(activities_xls, sheet_name='TASK')

print(activities_df)