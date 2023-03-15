import xlsxwriter as xl

def string_format(workbook,color='#FFFFFF',heading=False):
    format = None
    if heading == True:
        format = workbook.add_format( 
            {'bold': True,
            'font_color': 'white',
            'bg_color': color,
            'center_across': True,
            'text_wrap': True,
            'valign': 'vcenter',
            'border': 2}
        )
    else:
        format = workbook.add_format(
            {'bg_color': color,
            'border': 1}
        )
    return format

def number_format(workbook,color='#FFFFFF'):
    format = workbook.add_format(
        {'bg_color': color,
        'border': 1,
        'num_format': '_(* #,##0.00_);_(* (#,##0.00);_(* "-"??_);_(@_)'}
    )
    return format

def currency_format(workbook,color='#FFFFFF'):
    format = workbook.add_format(
        {'bg_color': color,
        'border': 1,
        'num_format': '_($* #,##0.00_);_($* (#,##0.00);_($* "-"??_);_(@_)'}
    )
    return format

def heading_format(workbook):
    format = workbook.add_format( 
        {'bold': True,
        'font_color': 'white',
        'bg_color': '#366092',
        'center_across': True,
        'text_wrap': True,
        'valign': 'vcenter',
        'border': 2}
    )
    return format

def heading_format1(workbook):
    format = workbook.add_format( 
        {'bold': True,
        'font_color': 'white',
        'bg_color': '#366092',
        }
    )
    return format


def heading_month_format(workbook):
    format = workbook.add_format( 
        {'bold': True,
        'font_color': 'white',
        'bg_color': '#366092',
        'center_across': True,
        'text_wrap': True,
        'valign': 'vcenter',
        'border': 2,
        'num_format': 'mmmm'}
    )
    return format

def percent_format(workbook,color):
    format = workbook.add_format(
        {'bg_color': color,
        'border': 1,
        'num_format': '0.00%'}
    )
    return format


def date_format(workbook,color):
    format = workbook.add_format(
        {'bg_color': color,
        'border': 1,
        'num_format': 'mm/dd/yyyy'}
    )
    return format

def month_format(workbook,color):
    format = workbook.add_format(
        {'bg_color': color,
        'border': 1,
        'num_format': 'mmmm'}
    )
    return format

def row_format1(workbook):
    format = workbook.add_format( 
        {'bold': True,
        'font_color': 'white',
        'bg_color': '#366092',
        }
    )
    return format

def row_format2(workbook):
    format = workbook.add_format( 
        {'bold': True,
        'font_color': 'black',
        'bg_color': '#D3D3D3',
        }
    )
    return format

def heading_format2(workbook):
    format = workbook.add_format( 
        {'bold': True,
        'font_color': 'black',
        'bg_color': 'white',
        'center_across': True,
        'text_wrap': True,
        'valign': 'vcenter',
        'border': 2}
    )
    return format

def heading_format3(workbook):
    format = workbook.add_format( 
        {'bold': True,
        'font_color': 'black',
        'bg_color': '#c3e3e2',
        'center_across': True,
        }
    )
    return format


def summary_text_light(workbook):
    format = workbook.add_format( 
        {'bold': True,
        'font_color': '#D3D3D3',
        }
    )
    return format

def summary_text_red(workbook):
    format = workbook.add_format( 
        {'bold': True,
        'font_color': 'black',
        'bg_color': 'red',
        }
    )
    return format

def summary_text_light_with_white_bg(workbook):
    format = workbook.add_format( 
        {'bold': True,
        'font_color': '#D3D3D3',
        'bg_color': 'white',
        }
    )
    return format
