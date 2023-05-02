import pandas as pd
import pickle


print('start importing')
cost_rprt_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Contract Forecasting Spreadsheet\Period 4 Export 04.29.23.xlsx')
cost_rprt_df = pd.read_excel(cost_rprt_xls)

sched_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Schedule\M007 Billing Cost Schedule - 05.01.23.xlsx')
cost_sched_df = pd.read_excel(sched_xls, sheet_name='Cost Forecast')
billing_sched_df = pd.read_excel(sched_xls, sheet_name='Billing Forecast')
sub_cost_df = pd.read_excel(sched_xls, sheet_name='Sub Cost Forecast')

activities_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\27 - PERSONAL FOLDERS\Brian Perez\Coney Island\03 - Schedule\Schedule March 2023.xlsx')
activities_df = pd.read_excel(activities_xls, sheet_name='TASK')

print('start saving')

with open('cost_rprt_df.pickle', 'wb') as f:
    pickle.dump(cost_rprt_df, f)
    
with open('cost_sched_df.pickle', 'wb') as f:
    pickle.dump(cost_sched_df, f)
    
with open('billing_sched_df.pickle', 'wb') as f:
    pickle.dump(billing_sched_df, f)
    
with open('sub_cost_df.pickle', 'wb') as f:
    pickle.dump(sub_cost_df, f)
    
with open('activities_df.pickle', 'wb') as f:
    pickle.dump(activities_df, f)
    
print('done')