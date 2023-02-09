import pandas as pd
import pickle


print('start importing')
cost_rprt_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Contract Forecasting Spreadsheet\Period 2 Export 02.07.23.xlsx')
cost_rprt_df = pd.read_excel(cost_rprt_xls)

sched_xls = pd.ExcelFile(r'C:\Users\bperez\Iovino Enterprises, LLC\M007-NYCHA-Coney Island Sites - Documents\General\08 - BUDGET & COST\Cost Codes\Schedule\M007 Billing Cost Schedule - 02.03.23.xlsx')
sched_df = pd.read_excel(sched_xls, sheet_name='Cost Forecast')
billing_sched_df = pd.read_excel(sched_xls, sheet_name='Billing Forecast')
sub_cost_df = pd.read_excel(sched_xls, sheet_name='Sub Cost Forecast')

print('start saving')

with open('cost_rprt_df.pickle', 'wb') as f:
    pickle.dump(cost_rprt_df, f)
    
with open('sched_df.pickle', 'wb') as f:
    pickle.dump(sched_df, f)
    
with open('billing_sched_df.pickle', 'wb') as f:
    pickle.dump(billing_sched_df, f)
    
with open('sub_cost_df.pickle', 'wb') as f:
    pickle.dump(sub_cost_df, f)
    
print('done')