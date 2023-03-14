from xlsxwriters.formats.standard_formats import *
import pandas as pd

def write_billing_forecast(workbook, worksheet, billing_df):
    for index, col in enumerate(billing_df.columns):
        if index > 4 and index < 15:
            worksheet.write(0, index, col, heading_month_format(workbook))
        else:
            worksheet.write(0, index, col, heading_format(workbook))


    for y in range(billing_df.shape[0]):
        for x in range(billing_df.shape[1]):
            if x < 3 or x > 15 and x != 18 and x != 23:
                worksheet.write(y+1, x, billing_df.iloc[y,x] if not pd.isna(billing_df.iloc[y,x]) else '', string_format(workbook, '#FFFFFF'))
            elif x == 18:
                worksheet.write(y+1, x, f"=P{y+2}/D{y+2}", percent_format(workbook, '#FFFFFF'))
            elif billing_df.columns[x] == 'Final Total':
                worksheet.write(y+1, x, f"=SUM(E{y+2}:O{y+2})", currency_format(workbook, '#FFFFFF'))
            elif billing_df.columns[x] == 'Total>Commitment?':
                worksheet.write(y+1, x, f"=P{y+2}>D{y+2}", string_format(workbook, '#FFFFFF'))
            else:
                worksheet.write(y+1, x, billing_df.iloc[y,x] if not pd.isna(billing_df.iloc[y,x]) else 0, currency_format(workbook, '#FFFFFF'))