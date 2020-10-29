import xlrd

# import xlrd
#
# book=xlrd.open_workbook('D:\\白平\\asd.xlsx','rb+')
# sheet=book.sheet_by_index(0)
# v=sheet.cell_value(1,1)
# for row in range(0,sheet.nrows):
#     for col in range(0,sheet.ncols):
#         print(sheet.cell_value(row,col))


# import  xlrd
# # #获取excel工作薄对象
# workbook=xlrd.open_workbook('D:\\白平\\asd.xlsx')#打开excel文件
# #获取sheet
# sheet=workbook.sheet_by_name('login')
# #获取value                                            python从excel读取的数据为数字时，自动加上.0转化为浮点型的解决
# value=sheet.cell_value(1,1)#第几行第几格,,,row行，col列
# print(value)
# # print(sheet.ncols)
# # # print(sheet.ncols)
class opertion:
    def __init__(self,path,name):
        self.workbook=xlrd.open_workbook(path)
        self.sheet=self.workbook.sheet_by_name(name)
    def get_nrow(self):
        return self.sheet.ncols
    def get_col(self):
        return  self.sheet.ncols
    def get_cell(self,row,col):
        return self.sheet.cell_value(row,col)