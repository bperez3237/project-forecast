from xlsxwriters.formats.standard_formats import *
import pandas as pd

def write_cost_forecast(workbook, worksheet, updated_df):
    for index, col in enumerate(updated_df.columns):
        worksheet.write(0, index, col, heading_format(workbook))


    for y in range(updated_df.shape[0]):
        for x in range(updated_df.shape[1]):
            if updated_df.columns[x] == 'Final Cost':
                # CHANGE THE LETTER ON THE END OF THE SUM AS THE MONTHS CHANGE
                worksheet.write(y+1, x, f"=SUM(D{y+2}:M{y+2})", currency_format(workbook, '#FFFFFF'))
            elif updated_df.columns[x] == 'Forecast Spent %':
                # CHANGE THE LETTER ON THE NUMERATOR AS THE MONTHS CHANGE
                worksheet.write(y+1, x, f"=IF(C{y+2}=0,0,N{y+2}/C{y+2})", percent_format(workbook, '#FFFFFF'))
                # worksheet.write(y+1, x, f"=N{y+2}/C{y+2}" if updated_df.iloc[y,2] != 0 else 0, percent_format(workbook, '#FFFFFF'))
            else:
                worksheet.write(y+1, x, updated_df.iloc[y,x] if not pd.isna(updated_df.iloc[y,x]) else 0, string_format(workbook, '#FFFFFF') if (x<2 or (x>=15 and x<18)) else currency_format(workbook, '#FFFFFF'))
