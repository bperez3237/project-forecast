import sys
import xlsxwriter as xl

from xlsxwriters.write_cost_forecast import write_cost_forecast
from utils.dataframe.add_codes import *
import import_data


def create_updated_sheet(cost_report_df, schedule_df):
    updated_df = add_codes_to_df(cost_report_df, schedule_df)

    workbook = xl.Workbook('Updated Schedule.xlsx')
    cost_forecast_worksheet = workbook.add_worksheet('Cost Forecast')
    write_cost_forecast(workbook, cost_forecast_worksheet, updated_df)
    workbook.close()

create_updated_sheet(cost_rprt_df, sched_df)

# print(sched_df)