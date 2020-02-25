# * coding:utf-8 *
# 作者           :heli 
# 创建时间       :2020/2/22  9:25
# 文件           :excel.py
# IDE            :PyCharm


import xlrd
import xlwt
from xlutils.copy import copy


def read_exel_sheet(sheet_name, filename):
    """
    读取表格
    :param sheet_name: sheet名字
    :param filename: 文件路径
    :return: xlrd.sheet.Sheet 格式
    """
    # 打开文件读取数据
    read_book = xlrd.open_workbook(filename)
    sheet = read_book.sheet_by_name(sheet_name)
    return sheet


def read_exel_row(row, sheet_name, filename):
    """
    读取表格一行数据
    :param sheet_name: sheet名字
    :param row: 行号
    :param filename: 文件路径
    :return: 一个list    ['','','']
    """
    # 打开文件读取数据
    read_book = xlrd.open_workbook(filename)
    return read_book.sheet_by_name(sheet_name).row_values(row)


def read_exel_cell_value(row, col, sheet_name, filename):
    """
    读取表格具体某个格子数据
    :param sheet_name:
    :param col: 列号
    :param row: 行号
    :param filename: 文件路径
    :return: 返回一个字符串
    """
    # 打开文件读取数据
    read_book = xlrd.open_workbook(filename)
    return read_book.sheet_by_name(sheet_name).cell_value(row, col)


def write_excel_cell(row, col, value, sheet_name, filename):
    """
    写excel 某个cell 内容
    :param row:
    :param col:
    :param value:
    :param sheet_name:
    :param filename:
    :return:
    """
    try:
        table = xlrd.open_workbook(filename)
        wb = copy(table)
        # wb.sheet_index(sheet_name)  获取sheet名字对应的序号
        #wb.get_sheet 根据序号获取sheet
        wb.get_sheet(wb.sheet_index(sheet_name)).write(row, col, value)
        wb.save(filename)
    except  Exception as e:
        print("写入exel %s出错" % filename)
        raise e


def new_exel_sheet(filename="data/demo.xls"):
    write_book = xlwt.Workbook()
    # write_book.sheet_index()
    write_sheet = write_book.add_sheet("Test sheet")
    write_sheet.write(1, 2, "ok2")
    write_book.save(filename)


if __name__ == '__main__':
    write_excel_cell(0, 1, 0, "Test sheet", "../data/demo.xls")
