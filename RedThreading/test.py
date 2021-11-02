import yaml
import xlrd

# file_path = r"D:\PythonProject\PythonProject\RedThreading\data.yaml"
# file = open(file_path,mode='r',encoding='utf-8')
# ys = yaml.load(file.read(),Loader=yaml.Loader)
# print(ys)
# device1 = ys.get('device1')
# print(device1)
# device1_list = device1[0]
# name = device1_list.get('name')
# port = device1_list.get('port')
# print('设备名:',name,'端口号:',port)

path = r'D:\PythonProject\PythonProject\RedThreading\devices.xls'
file = xlrd.open_workbook(path)
sheet = file.sheet_by_index(0)
for i in range (3):
    row_list = sheet.row_values(i)
    if '' not in row_list:
        name = str(row_list[1])
        version = int(row_list[2])
        port = int(row_list[3])
        print(name,version,port)
    else:
        name = str(row_list[1])
        version = row_list[2]
        port = row_list[3]
        print(name,version,port)



