# -*- coding: utf-8 -*-
import xlrd
import xlwt
#from xlutils.copy import copy
def str2hex(s):
    odata = 0;
    su =s.upper()
    for c in su:
        tmp=ord(c)
        if tmp <= ord('9'):
            odata = odata << 4
            odata += tmp - ord('0')
        elif ord('A') <= tmp <= ord('F'):
            odata = odata << 4
            odata += tmp - ord('A') + 10
    return odata
'''Read Excel data and define dict'''
def read_excel(path,sheetname,row,column)
    # 打开文件
    workbook = xlrd.open_workbook(path)
    # 获取所有sheet
    sheet = workbook.sheet_by_name(sheetname)
    value = sheet.cell_value(row,column)
    return value
def GetExcel_row_col(path,sheetname,row,column):
    list_row_col =[]
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheet_by_name(sheetname)
    row = sheet.nrows
    col = sheet.ncols
    list_row_col.append(row)
    list_row_col.append(col)
    return list_row_col
def Excel_handle(path,str1,str2):
    '''
    :param path:excel exsit path to get freamtype
    :param str1:excel_cell() string value
    :param str2:string to save freamtype value
    :return:type(dict)include id,data,length
    '''
    if "Beacon" in path:
        str2 = "Beacon"
    elif "Probe" in path:
        str2 = "Probe Response"
    elif "Auth" in path:
        str2 = "Authentication Response"
    elif "Assoc" in path:
        str2 = "Associate Response"
    id = str2hex(str1[:2])
    length = str2hex(str1[2:4])
    data = str1[4:]
    Dict_value = dict([('data',data),('frame_type',str2),('id',id),('length',length)])
    return Dict_value
