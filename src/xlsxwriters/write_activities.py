from xlsxwriters.formats.standard_formats import *
import pandas as pd

def write_activities(workbook, worksheet, activities_df):
    for index, col in enumerate(activities_df.columns):
        worksheet.write(0, index, col, heading_format(workbook))


    for y in range(activities_df.shape[0]):
        for x in range(activities_df.shape[1]):
            # if activities_df.columns[x] == 'week start' or activities_df.columns[x] == 'week end':
            #     worksheet.write(y+1, x, f"=SUM(D{y+2}:M{y+2})", currency_format(workbook, '#FFFFFF'))
            # else:
            worksheet.write(y+1, x, activities_df.iloc[y,x] if not pd.isna(activities_df.iloc[y,x]) else 0, string_format(workbook, '#FFFFFF') if (x < 15) else date_format(workbook, '#FFFFFF'))