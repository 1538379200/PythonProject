import os
import xlrd

path = os.path.abspath('.')
file_path = path+r'\dbsetting.xls'
wb = xlrd.open_workbook(file_path)
sheet = wb.sheet_by_index(0)
host = sheet.cell_value(1,0)
port = int(sheet.cell_value(1,1))
username = sheet.cell_value(1,2)
pwd = sheet.cell_value(1,3)
dbname = sheet.cell_value(1,4)
print(host,port,username,pwd,dbname)