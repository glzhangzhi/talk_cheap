本文介绍的是openpyxl这个库，我一直使用这个库进行python语言上的excel文件交互，包括读写等操作。
[http://bitbucket.org/openpyxl/openpyxl/src](http://bitbucket.org/openpyxl/openpyxl/src)
以上是源码地址

该库支持的文件格式有xls/xlsx/xlsm/xltx/xltm
```
pip install openpyxl
```
如果需要在表格文件中插入图片，需要额外安装pillow库

```python
from openpyxl import Workbook #导入库
wb = Workbook() #创建表格
ws = wb.active #激活表单
ws1 = wb.create_sheet('sheet1', -1) #在最后一个位置创建名为sheet1的表单
ws.title = 'New Title' #将此表单名更改
ws = wb['sheet1'] #创建sheet1表单的对象
c = ws['A4'] #将A4单元格赋予c
ws['A4'] = 4 #赋值给A4单元格
d = ws.cell(row=4, colum=2, value=10) #用行列定位单元格
cell_range = ws['A1':'C2'] #单元格区域选择
colC = ws['C'] #选择整列
col_range = ws['C:D'] #选择两列，注意引号
row10 = ws[10] #选择整行
row_range = ws[5:10] #选择复数行
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2): #迭代单元格
    for cell in row:
        print(cell)
for col in ws.iter_cols():
    for cell in col:
        print()
for row in ws.values:
    for value in row:
       print(value)
c.value = 4 #选择单元格的值
print(c.value)
wb.save('data.xlsx') #保存表格
wb = load_workbook('test.xlsx') #读取表格
```