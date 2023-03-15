from xlsxwriters.formats.standard_formats import *
from utils.dataframe.dataframe_utils import get_col_widths
import pandas as pd

def write_cost_forecast(workbook, worksheet, updated_df):
    for index, col in enumerate(updated_df.columns):
        if "Unnamed" in col: 
            continue
        worksheet.write(0, index, col, heading_format(workbook))


    for y in range(updated_df.shape[0]):
        for x in range(updated_df.shape[1]):
            if "Unnamed" in updated_df.columns[x]: 
                continue
            
            if updated_df.columns[x] == 'Final Cost':
                # CHANGE THE LETTER ON THE END OF THE SUM AS THE MONTHS CHANGE
                worksheet.write(y+1, x, f"=SUM(D{y+2}:N{y+2})", currency_format(workbook, '#FFFFFF'))
            elif updated_df.columns[x] == 'Forecast Spent %':
                # CHANGE THE LETTER ON THE NUMERATOR AS THE MONTHS CHANGE
                worksheet.write(y+1, x, f"=IF(C{y+2}=0,0,O{y+2}/C{y+2})", percent_format(workbook, '#FFFFFF'))
            else:
                worksheet.write(y+1, x, updated_df.iloc[y,x] if not pd.isna(updated_df.iloc[y,x]) else 0, string_format(workbook, '#FFFFFF') if (x<2 or (x>=16 and x<19)) else currency_format(workbook, '#FFFFFF'))
                
    for i, width in enumerate(get_col_widths(updated_df)):
        worksheet.set_column(i-1, i-1, width)
