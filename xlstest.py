__author__ = 'mitrikyle'
import xlrd

workbook = xlrd.open_workbook('test.xlsx')

worksheet = workbook.sheet_by_index(0)

# for each person
for x in range(2,10):
    for y in range(1,3):
        print worksheet.cell(x,y).value