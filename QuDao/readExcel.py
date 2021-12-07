import xlrd

# workbook = xlrd.open_workbook(filename=r'C:\Users\Admin\PycharmProjects\testDemo\QuDao\关联固定渠道.xls')
# table = workbook.sheet_by_name(sheet_name='Sheet1')
# rows = table.nrows
# cols = table.ncols
# for row in range(rows):
#     for col in range(cols):
#         value = table.cell_value(row, col)
#        print('第{}行{}列的数据为：{}'.format(row, col, value))
def xlrd_excel():
    data = xlrd.open_workbook(r'C:\Users\Admin\PycharmProjects\testDemo\QuDao\关联固定渠道.xls')  # 打开xls文件
    table = data.sheet_by_name(u'Sheet1') #通过名称获取
    nrows=table.nrows  # 获取表的行数
    li=[]
    for i in range(nrows):     # 循环逐行打印
        if i!=0:        #跳过第一行
            li.append(str(table.row_values(i)))
    return li        #将取回的值放入列表中
print (xlrd_excel())
