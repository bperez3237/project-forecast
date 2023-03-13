import numpy as np
import xlsxwriter as xl
import pandas as pd
from datetime import date
import pprint as pp
import math


def sub_dictionary(billing_df, activities_df, sub_list):
    dic = {sub: {} for sub in sub_list}
    for y in range(billing_df.shape[0]):
        if not pd.isna(billing_df['Category 1'][y]):
            if billing_df['Category 1'][y] in dic[billing_df['Sub'][y]]:
                if billing_df['SOV Level 1'][y] not in dic[billing_df['Sub'][y]][billing_df['Category 1'][y]]:
                    dic[billing_df['Sub'][y]][billing_df['Category 1'][y]][billing_df['SOV Level 1'][y]] = None
            else:
                dic[billing_df['Sub'][y]][billing_df['Category 1'][y]] = {}
                dic[billing_df['Sub'][y]][billing_df['Category 1'][y]][billing_df['SOV Level 1'][y]] = None


    for y in range(activities_df.shape[0]):
        if not pd.isna(activities_df['Category 1'][y]):
            if activities_df['Category 1'][y] in dic[activities_df['Sub'][y]]:
                if activities_df['Area'][y] not in dic[activities_df['Sub'][y]][activities_df['Category 1'][y]]:
                    dic[activities_df['Sub'][y]][activities_df['Category 1'][y]][activities_df['Area'][y]] = None
            else:
                dic[activities_df['Sub'][y]][activities_df['Category 1'][y]] = {}
                dic[activities_df['Sub'][y]][activities_df['Category 1'][y]][activities_df['Area'][y]] = None

    return dic

