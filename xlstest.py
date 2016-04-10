__author__ = 'mitrikyle'
import xlrd
from peeps import Person
import peeps
workbook = xlrd.open_workbook('test.xlsx')

worksheet = workbook.sheet_by_index(0)

# for each person
#cell(row, column)
people = []
for x in range(2,139):
    name = worksheet.cell(x,1).value + " " + worksheet.cell(x,2).value
    number = worksheet.cell(x,4).value
    halls = []
    if str(worksheet.cell(x,5)).split(":")[1].replace("'", "") == "Any":
        halls.append("De Neve")
        halls.append("B-Plate")
        halls.append("Covel")
    else:
        for y in range(6, 9):
            if str(worksheet.cell(x,y)).split(":")[1].replace("'", ""):
                halls.append(str(worksheet.cell(x,y)).split(":")[1].replace("'", ""))
    times = []
    for z in range(9, 12+1):
        timeString = (str(worksheet.cell(x,z)).split(":")[1].replace("'", ""))
        if timeString:
            times.append(int(timeString))
    peep = Person(name, times, halls, number)
    people.append(peep)
print(len(people))

peeps.test(people)



