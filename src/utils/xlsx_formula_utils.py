from utils.string_utils import add_to_letter

def work_billing_summary_formula(row, col_index, sub_row, index_2, index_3):
    return (f"=SUMIFS('Billing Forecast'!{add_to_letter('F', col_index)}:{add_to_letter('F', col_index)},'Billing Forecast'!$T:$T,$A${sub_row+1},'Billing Forecast'!$U:$U,$B${row-index_3*3},'Billing Forecast'!$Q:$Q,$C{row+1})/SUMIFS('Billing Forecast'!$D:$D,'Billing Forecast'!$T:$T,$A${sub_row+1},'Billing Forecast'!$U:$U,$B${row-index_3*3},'Billing Forecast'!$Q:$Q, $C{row+1})")

def work_cost_summary_formula(row, col_index, sub_row, index_2, index_3, sub):
    if sub == 'MLJ':
        # MISSING AREA/SOV1 COLUMN BACK INTO MLJ COST FORECAST 
        return (f"=SUMIFS('Cost Forecast'!{add_to_letter('F', col_index)}:{add_to_letter('F', col_index)},'Cost Forecast'!$R:$R,$B${row-index_3*3},'Cost Forecast'!$Q:$Q,$C{row+1})/SUMIFS('Cost Forecast'!$D:$D,'Cost Forecast'!$R:$R,$B${row-index_3*3},'Cost Forecast'!$Q:$Q, $C{row+1})")
    else:
        #NEED TO ADD CATEGORY COLUMN TO SUB COST FORECAST IMPORT DF
        #UPDATE SUB COST FORECAST TO INCLUDE AREA IN THE RIGHT FORMAT
        return (f"=SUMIFS('Sub Cost Forecast'!{add_to_letter('G', col_index)}:{add_to_letter('G', col_index)},'Sub Cost Forecast'!$U:$U,$A${sub_row+1},'Sub Cost Forecast'!$W:$W,$B${row-index_3*3},'Sub Cost Forecast'!$R:$R,$C{row+1})/SUMIFS('Sub Cost Forecast'!$D:$D,'Sub Cost Forecast'!$U:$U,$A${sub_row+1},'Sub Cost Forecast'!$W:$W,$B${row-index_3*3},'Sub Cost Forecast'!$R:$R, $C{row+1})")

