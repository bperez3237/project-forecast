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

# print(activities_df.columns)
# print(cost_sched_df.columns)
# print(billing_sched_df.columns)

# print(cost_sched_df['Category 1'].unique())
# print(billing_sched_df['Category 1'].unique())
# print(cost_sched_df['Category 1'].unique() + billing_sched_df['Category 1'].unique() + activities_df['Category'].unique())

data_dic = {
    'SITE': {
            'ACTIVITIES': {

            },
            'BILLINGS': {

            },
            'COSTS': {

            }
    },
    'NEW BUILDINGS': {
            'ACTIVITIES': {

            },
            'BILLINGS': {

            },
            'COSTS': {
                
            }
    },
    'EXISTING BUILDINGS': {
            'ACTIVITIES': {

            },
            'BILLINGS': {

            },
            'COSTS': {
                
            }
    }
}
# print(activities_df.columns)
for y in range(activities_df.shape[0]):
    if activities_df['Activity Status'][y] != 'Completed' and activities_df['CODE TYPE'][y] == 'CONSTRUCTION':

        if activities_df['Category'][y].upper() == 'SITE' or activities_df['Category'][y].upper() == 'NEW BUILDINGS' or activities_df['Category'][y].upper() == 'EXISTING BUILDINGS':
            data_dic[activities_df['Category'][y].upper()]['ACTIVITIES'][activities_df['Activity ID'][y]] = {
                'start_date': activities_df['(*)Start'][y],
                'end_date': activities_df['(*)Finish'][y],
                'activity_name': activities_df['Activity Name'][y],
            }

pp.pprint(data_dic)
# turn pandas series into object
def series_to_object(series):
    return series.to_dict()