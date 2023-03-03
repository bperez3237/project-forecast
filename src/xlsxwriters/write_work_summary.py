from xlsxwriters.formats.standard_formats import *
from utils.dataframe.sub_dictionary import sub_dictionary
from utils.xlsx_formula_utils import work_billing_summary_formula, work_cost_summary_formula
import pandas as pd
from utils.date_utils import business_days, days_in_month
from datetime import date, timedelta as td, datetime as dt

# def 


def write_work_summary(workbook, worksheet, billing_sched_df, activities_df):
    worksheet.write(0,0, 'Subcontractor', heading_format(workbook))
    worksheet.write(0,1, 'Category', heading_format(workbook))
    worksheet.write(0,2, 'Building', heading_format(workbook))
    worksheet.write(0,3, 'Type', heading_format(workbook))
    worksheet.write(0,4, 'February', heading_format(workbook))
    worksheet.write(0,5, 'March', heading_format(workbook))
    worksheet.write(0,6, 'April', heading_format(workbook))
    worksheet.write(0,7, 'May', heading_format(workbook))
    worksheet.write(0,8, 'June', heading_format(workbook))
    worksheet.write(0,9, 'July', heading_format(workbook))
    worksheet.write(0,10, 'August', heading_format(workbook))
    worksheet.write(0,11, 'September', heading_format(workbook))
    worksheet.write(0,12, 'October', heading_format(workbook))


    sub_list = pd.concat([billing_sched_df['Sub'],activities_df['Sub']], axis = 0).dropna().unique().tolist()
    sub_list.sort()

    sub_dic = sub_dictionary(billing_sched_df, activities_df, sub_list)
    
    row = 1
    for index_x, subcontractor in enumerate(sub_dic):
        # print(subcontractor)
        
        worksheet.write(row, 0, subcontractor)
        sub_row = row
        row += 1
        for index_y,category in enumerate(sub_dic[subcontractor]):
            # print(category)
            
            worksheet.write(row, 1, category)
            row += 1
            for index_z,area in enumerate(sub_dic[subcontractor][category]):
                # print(area)
                
                worksheet.write(row, 2, area)
                worksheet.write(row, 3, 'Billings')
                #range 0-9 for jan-oct
                for col_index in range(9):
                    worksheet.write(row,4+col_index,(work_billing_summary_formula(row, col_index, sub_row, index_y, index_z)), percent_format(workbook, '#ffffff'))
                    
                worksheet.write(row+1, 3, 'Costs')
                for col_index in range(9):
                    worksheet.write(row+1,4+col_index,(work_cost_summary_formula(row, col_index, sub_row, index_y, index_z, subcontractor)), percent_format(workbook, '#ffffff'))

                worksheet.write(row+2, 3, 'Activities')
                for col_index in range(9):
                    filtered_df = activities_df.loc[activities_df['Sub'] == subcontractor].loc[activities_df['Category 1'] == category].loc[activities_df['Area'] == area]
                    months_array = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October']
                    total_days_in_month = 0
                    for start, end in zip(filtered_df['(*)Start'], filtered_df['(*)Finish']):
                        total_days_in_month += days_in_month(col_index+1, start, end)
                        
                
                    total_days = 0
                    for start, end in zip(filtered_df['(*)Start'], filtered_df['(*)Finish']):
                        total_days += (end - start).total_seconds() / 86400
                        
                    worksheet.write(row+2,4+col_index, total_days_in_month/total_days if total_days != 0 else 0, percent_format(workbook, '#ffffff'))
                
                row += 3