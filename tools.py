import xlrd
import random
 

'''pip install xlrd==1.2.0'''

data = xlrd.open_workbook(r'imEx.xlsx')

sheet1 = data.sheet_by_index(0)#通过索引获取表格

maxrows = sheet1.nrows  

def randExcel():
    rowNum = random.randint(0,maxrows-1)
    print("随机获取列数：",rowNum)
    rows = sheet1.row_values(rowNum)
    return rows[0],rows[1]

def get_sex(self):
         #男生：1 女生：2
         num = int(self[16:17])
         if num % 2 == 0:
             return 2
         else:
             return 1


