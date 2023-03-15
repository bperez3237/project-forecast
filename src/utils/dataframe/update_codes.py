import numpy as np
import xlsxwriter as xl
import pandas as pd
from datetime import date
import pprint as pp
import math
# from .dataframe_utils import array_differences


def array_differences(array1, array2) -> list:
    #return an array values which not shared between the two arrays
    return [x for x in array1 if x not in array2] + [x for x in array2 if x not in array1]



def add_codes_to_df(cost_report_df: pd.DataFrame, schedule_df: pd.DataFrame) -> pd.DataFrame:
    missing_codes = array_differences(schedule_df['Code'].unique(), cost_report_df['Phase'].unique())
    updated_report_df = schedule_df
    for code in missing_codes:
        code_data = cost_report_df[cost_report_df['Phase'] == code]
        code_dict = {key: 0 for key in schedule_df.columns}
        code_dict.update({
            'Code':code, 
            'Name': code_data['Name'].values[0],
            'Projected Forecast': code_data['Projected Cost Forecast'].sum(),
            'Spent to Date': code_data['Actual Cost'].sum(),

        })
        updated_report_df = pd.concat([updated_report_df, pd.DataFrame(code_dict, index=[0])], ignore_index=True)

    return updated_report_df.sort_values(by=['Code'])

def update_codes(cost_report_df: pd.DataFrame, cost_sched_df: pd.DataFrame) -> pd.DataFrame:
    for y in range(cost_sched_df.shape[0]):
        cost_sched_df.iloc[y,2] = cost_report_df[cost_report_df['Phase'] == cost_sched_df.iloc[y,0]]['Projected Cost Forecast'].sum()
        cost_sched_df.iloc[y,3] = cost_report_df[cost_report_df['Phase'] == cost_sched_df.iloc[y,0]]['Actual Cost'].sum()
        
    return cost_sched_df