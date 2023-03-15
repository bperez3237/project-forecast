from xlsxwriters.formats.standard_formats import *
from utils.dataframe.sub_dictionary import sub_dictionary
from utils.xlsx_formula_utils import work_billing_summary_formula, work_cost_summary_formula
import pandas as pd
from utils.date_utils import business_days, days_in_month
from datetime import date, timedelta as td, datetime as dt
from utils.letter_utils import letter_to_index, index_to_letter


def write_forecast_summary(workbook, worksheet):
    for col in range(1,12):
        worksheet.write(1, col, 'Cost' if col==1 else '', heading_format1(workbook))
    
    worksheet.write(2, 1, '', heading_format3(workbook))
    
    worksheet.write(3, 1, 'Labor', string_format(workbook, '#FFFFFF'))
    worksheet.write(4, 1, 'Equipment', string_format(workbook, '#FFFFFF'))
    worksheet.write(5, 1, 'Subcontractor', string_format(workbook, '#FFFFFF'))
    worksheet.write(6, 1, 'Consumable/Material', string_format(workbook, '#FFFFFF'))
    worksheet.write(7, 1, 'Overhead', string_format(workbook, '#FFFFFF'))
    worksheet.write(8, 1, 'Total', string_format(workbook, '#FFFFFF'))
    
    for col in range(1,12):
        worksheet.write(10, col, 'Billing' if col==1 else '', heading_format1(workbook))
    
    worksheet.write(11, 1, '', heading_format3(workbook))
    
    worksheet.merge_range('C18:E18', 'Annual Billing and Cost',  heading_format(workbook))
    
    worksheet.write(12, 1, 'Total', string_format(workbook, '#FFFFFF'))
    worksheet.write(14, 1, 'Profit Variance', string_format(workbook, '#FFFFFF'))
    
    worksheet.write(18, 2, 'Billing', string_format(workbook, '#FFFFFF'))
    worksheet.write(18, 3, 'Cost', string_format(workbook, '#FFFFFF'))
    worksheet.write(18, 4, 'Profit', string_format(workbook, '#FFFFFF'))
    worksheet.write(19, 1, '2020 Total', string_format(workbook, '#FFFFFF'))
    worksheet.write(20, 1, '2021 Total', string_format(workbook, '#FFFFFF'))
    worksheet.write(21, 1, '2022 Total', string_format(workbook, '#FFFFFF'))
    worksheet.write(22, 1, '2023 Total', string_format(workbook, '#FFFFFF'))
    worksheet.write(23, 1, 'Final Total', string_format(workbook, '#FFFFFF'))
    
    
    column = 2
    for month in range(2, 12):
        letter1 = index_to_letter(column+2).upper()
        letter2 = index_to_letter(column+4).upper()
        letter3 = index_to_letter(column+3).upper()
        letter4 = index_to_letter(column).upper()
        cost_text = lambda x: f"=SUMIF('Cost Forecast'!Q:Q,{x},'Cost Forecast'!{letter1}:{letter1})"
        worksheet.write(2, column, dt(2019, month+1, 1).strftime('%B'), heading_format3(workbook))
        worksheet.write(3, column, cost_text("B4") , currency_format(workbook))
        worksheet.write(4, column, cost_text("B5") , currency_format(workbook))
        worksheet.write(5, column, f"=SUM('Sub Cost Forecast'!{letter2}:{letter2})", currency_format(workbook))
        worksheet.write(6, column, cost_text('\"Material\"') , currency_format(workbook))
        worksheet.write(7, column, cost_text("B8") , currency_format(workbook))
        worksheet.write(8,column, f"=SUM({letter4}4:{letter4}8)", currency_format(workbook))
        
        worksheet.write(11, column, dt(2019, month, 1).strftime('%B'), heading_format3(workbook))
        worksheet.write(12, column, f"=SUM('Billing Forecast'!{letter3}:{letter3})", currency_format(workbook))
        worksheet.write(14, column, f"={letter4}13-{letter4}9", currency_format(workbook))
        
        
        column += 1
   
   
    letterC = index_to_letter(2).upper()
    letterD = index_to_letter(3).upper()
    worksheet.write(19,2, 5_189_506, currency_format(workbook))
    worksheet.write(19,3, 1_813_875.69, currency_format(workbook))
    worksheet.write(19,4, f"={letterC}20-{letterD}20", currency_format(workbook))
    
    worksheet.write(20,2, 40_215_999.85, currency_format(workbook))
    worksheet.write(20,3, 36_132_226.23, currency_format(workbook))
    worksheet.write(20,4, f"={letterC}21-{letterD}21", currency_format(workbook))

    
    worksheet.write(21,2, 89_644_456.90, currency_format(workbook))
    worksheet.write(21,3, 81_147_688.19, currency_format(workbook))
    worksheet.write(21,4, f"={letterC}22-{letterD}22", currency_format(workbook))

    worksheet.write(22,2, "=SUM(C9:L9)", currency_format(workbook))
    worksheet.write(22,3, '=SUM(C13:L13)', currency_format(workbook))    
    worksheet.write(22,4, f"={letterC}23-{letterD}23", currency_format(workbook))

    worksheet.write(23,2, f"=SUM({letterC}20:{letterC}23)", currency_format(workbook))
    worksheet.write(23,3 , f"=SUM({letterD}20:{letterD}23)", currency_format(workbook))
    worksheet.write(23, 4 , f"={letterC}24-{letterD}24", currency_format(workbook))
    
    worksheet.set_column(0,23,None)