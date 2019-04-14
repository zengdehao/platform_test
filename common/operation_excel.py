import xlrd
from xlutils.copy import copy
from datetime import date, datetime
import os
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class OperationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = current_dir+'\\datacase\\test2.xls'
            self.sheet_id = 0
        self.data = self.get_data()
    
    # 获取sheets的内容
    def get_data(self):
        self.workbook = xlrd.open_workbook(self.file_name)
        tables = self.workbook.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        return self.data.nrows

    # 获取某一行的数据
    def get_row_values(self,row):
        return self.data.row_values(row)
        
    # 获取某一列的数据
    def get_col_values(self,col=None):
        if col != None:
            col_data = self.data.col_values(col)
        else:
            col_data = self.data.col_values(0)
        return col_data
        
    # 获取单元格的数据类型
    def get_cell_ctype(self,row,col):
        return self.data.cell(row,col).ctype
        
    # 获取某个单元格的内容
    def get_cell_value(self,row,col):
        # 读取日期格式的特殊处理
        if self.get_cell_ctype(row,col) == 3:
            date_value = xlrd.xldate_as_tuple(self.data.cell_value(row,col),self.workbook.datemode)
            get_value = date(*date_value[:3]).strftime('%Y/%m/%d') 
        else:
            get_value = self.data.cell_value(row,col)
        return get_value

    # 写入数据
    def write_value(self,row,col,value):
        '''
        写入Excel数据
        :param row:
        :param col:
        :param value:
        :return:
        '''
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row,col,value)
        write_data.save(self.file_name)

    '''
    对于依赖数据的处理
    1，根据要执行的的用例的行号获取所依赖的用例的case_id（获取单元格的内容）
    2，获取case_id所在列的所有内容（获取某一列的内容）
    3，根据case_id获取所依赖的用例所在列的行号
    4，根据行号获取依赖用例的行的内容（获取某一行的内容）
    5，根据行的内容请求接口获取返回数据
    1-4涉及到对Excel文件的操作  
    '''

    # 根据对应的case_id获取所依赖的用例对应的行号
    def get_row_num(self,case_id):
        num = 0
        cols_data = self.get_col_values()
        for col_data in cols_data:
            if case_id == col_data:
                return num
            num += 1

    # 根据所获取的行号获取依赖用例的行的内容
    def get_row_data(self,case_id):
        row = self.get_row_num(case_id)
        row_data = self.get_row_values(row)
        return row_data




if __name__ == '__main__':
    opers = OperationExcel()
    key = opers.get_cell_value(3,6)
    num = opers.get_row_num(key)
    print(key)
    print(num)
    

