# * coding:utf-8 *
# 作者           :heli 
# 创建时间       :2020/2/22  9:25
# 文件           :rw_exel.py
# IDE            :PyCharm


import xlrd
import xlwt


def read_exel(filename="data/demo.xls"):
    """
    读取表格
    :param filename: 文件路径
    :return: xlrd.sheet.Sheet 格式
    """
    #打开文件读取数据
    read_book = xlrd.open_workbook(filename)
    sheet= read_book.sheet_by_name("Test sheet")
    return sheet


def write_exel(filename="data/demo.xls"):
    write_book = xlwt.Workbook()
    write_sheet = write_book.add_sheet("Test sheet")
    write_sheet.write(1,2,"ok2")
    write_book.save(filename)



if __name__ == '__main__':
    sheet=read_exel(filename="../data/demo.xls")
    print(type(sheet))
    write_exel(filename="../data/demo.xls")
