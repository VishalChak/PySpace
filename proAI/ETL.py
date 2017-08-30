# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 19:20:53 2017

@author: 10639497
"""

import pandas as pd
import constant

def read_data(file_path,data_type,sep=',', index_col=0, parse_dates=True,infer_datetime_format=True):
    file_type= data_type.lower()
    if (file_type == constant.CSV):
        return pd.read_csv(file_path,sep,index_col,parse_dates,infer_datetime_format)
    elif(file_type == constant.JSON):
        return pd.read_json(file_path,index_col,parse_dates,infer_datetime_format)
    elif(file_type == constant.MS_Excel):
        pd.read_excel(file_path,sheetname=0,header)

if __name__ == "__main__":
    