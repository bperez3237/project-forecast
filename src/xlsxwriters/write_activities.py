from xlsxwriters.formats.standard_formats import *
from utils.dataframe.dataframe_utils import get_col_widths
import pandas as pd

def write_activities(workbook, worksheet, activities_df):
    for index, col in enumerate(activities_df.columns):
        if "Unnamed" in col: 
            continue
        worksheet.write(0, index, col, heading_format(workbook))


    for y in range(activities_df.shape[0]):
        for x in range(activities_df.shape[1]):
            xlsx_index = y+2
            if "Unnamed" in activities_df.columns[x]: 
                continue
            
            if ('week start' in activities_df.columns[x] or 'week end' in activities_df.columns[x]) and y > 0:
                continue
                
            if activities_df.columns[x] == '(*)Total Float(h)' or activities_df.columns[x] == 'Original Duration(h)' or activities_df.columns[x] == 'Remaining Duration(h)':
                worksheet.write(y+1, x, activities_df.iloc[y,x] if not pd.isna(activities_df.iloc[y,x]) else '', number_format(workbook, '#FFFFFF'))
            elif activities_df.columns[x] == 'During Week':
                worksheet.write(y+1, x, f"=OR(AND(P{xlsx_index}<=U$2,Q{xlsx_index}>V$2),AND(P{xlsx_index}>U$2,P{xlsx_index}<V$2))", string_format(workbook))
            else:
                worksheet.write(y+1, x, activities_df.iloc[y,x] if not pd.isna(activities_df.iloc[y,x]) else '', string_format(workbook, '#FFFFFF') if (x < 15) else date_format(workbook, '#FFFFFF'))
    
    
    for i, width in enumerate(get_col_widths(activities_df)):
        worksheet.set_column(i-1, i-1, width)