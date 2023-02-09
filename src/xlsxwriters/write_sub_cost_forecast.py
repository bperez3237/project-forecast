from xlsxwriters.formats.standard_formats import *
import pandas as pd

def write_sub_cost_forecast(workbook, worksheet, updated_df):
    for index, col in enumerate(updated_df.columns):
        if index > 5 and index < 16:
            worksheet.write(0, index, col, heading_month_format(workbook))
        else:
            worksheet.write(0, index, col, heading_format(workbook))


    for y in range(updated_df.shape[0]):
        for x in range(updated_df.shape[1]):
            if x < 3 or x > 16 and x != 19:
                worksheet.write(y+1, x, updated_df.iloc[y,x] if not pd.isna(updated_df.iloc[y,x]) else 0, string_format(workbook, '#FFFFFF'))
            elif x == 19:
                worksheet.write(y+1, x, f"=P{y+2}/D{y+2}", percent_format(workbook, '#FFFFFF'))
            elif updated_df.columns[x] == 'Final Total':
                worksheet.write(y+1, x, f"=SUM(E{y+2}:O{y+2})", currency_format(workbook, '#FFFFFF'))
            else:
                worksheet.write(y+1, x, updated_df.iloc[y,x] if not pd.isna(updated_df.iloc[y,x]) else 0, currency_format(workbook, '#FFFFFF'))