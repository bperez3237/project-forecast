import sys
import pickle
import xlsxwriter as xl
from xlsxwriters.write_cost_forecast import write_cost_forecast
from xlsxwriters.write_billing_forecast import write_billing_forecast
from xlsxwriters.write_sub_cost_forecast import write_sub_cost_forecast
from utils.dataframe.add_codes import add_codes_to_df
# from data.import_data import cost_rprt_df, sched_df, billing_sched_df, sub_cost_df


with open('cost_rprt_df.pickle', 'rb') as f:
    cost_rprt_df = pickle.load(f)
with open('sched_df.pickle', 'rb') as f:
    sched_df = pickle.load(f)
with open('billing_sched_df.pickle', 'rb') as f:
    billing_sched_df = pickle.load(f)
with open('sub_cost_df.pickle', 'rb') as f:
    sub_cost_df = pickle.load(f)


updated_cost_df = add_codes_to_df(cost_rprt_df, sched_df)

workbook = xl.Workbook('Updated Schedule.xlsx')
cost_forecast_worksheet = workbook.add_worksheet('Cost Forecast')
write_cost_forecast(workbook, cost_forecast_worksheet, updated_cost_df)
    
billing_forecast_worksheet = workbook.add_worksheet('Billing Forecast')
write_billing_forecast(workbook, billing_forecast_worksheet, billing_sched_df)
    
sub_cost_forecast_worksheet = workbook.add_worksheet('Sub Cost Forecast')
write_sub_cost_forecast(workbook, sub_cost_forecast_worksheet, sub_cost_df)
    
    
workbook.close()

# write_workbook(cost_rprt_df, sched_df)

# print(sub_cost_df)

