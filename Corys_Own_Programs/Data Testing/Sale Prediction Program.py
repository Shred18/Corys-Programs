#Write a program that predicts the day of a sale (Monday-Sunday) based off 1 year of previous data
import xlrd
import pandas as pd
from matplotlib import pyplot as plt

Excelsheet1 = 'SALESTEST.xlsx' #just setting the variable name
book = xlrd.open_workbook(Excelsheet1) #opening the excel sheet for manipulating purposes

graph = pd.read_excel('SALESTEST.xlsx') #allows you to create the graph
plt.title('Yearly sales') #set title
plt.xlabel('Occurances of day in the year') #X axis
plt.ylabel('Total sales accumulated') #Y axis

first_sheet = book.sheet_by_index(0) #telling python to just look at the first sheet

print(first_sheet.row_values(0)) #prints first row, usually the header

headings = first_sheet.row_values(0)
column2heading = headings[0]
print(column2heading)

i = 0
total = 0

for row in range(first_sheet.nrows): #looking at all
    if str(first_sheet.cell(row,0).value) == 'Monday': #checking for the day to equal monday
        i = i + 1 #counting the total number of mondays
        total = total + (first_sheet.cell(row,1).value) #adding the sales for each monday to the total
        print("total i is now", i)
        print('total sales is now', total)
        plt.plot(i, total, 'o', color = 'red')
    else:
        pass
averagemon = total / i
print('Mondays Average is', averagemon)


i = 0
total = 0
for row in range(first_sheet.nrows): #looking at all
    if str(first_sheet.cell(row,0).value) == 'Tuesday':
        i = i + 1
        total = total + (first_sheet.cell(row,1).value)
        print("total i is now", i)
        print('total sales is now', total)
        plt.plot(i, total, 'o', color = 'blue')
    else:
        pass
averagetue = total / i
print('Tuesdays Average is', averagetue)

i = 0
total = 0
for row in range(first_sheet.nrows): #looking at all
    if str(first_sheet.cell(row,0).value) == 'Wednesday':
        i = i + 1
        total = total + (first_sheet.cell(row,1).value)
        print("total i is now", i)
        print('total sales is now', total)
        plt.plot(i,total, 'o', color = 'black')
    else:
        pass
averagewed = total / i
print('Wednesday Average is', averagewed)

i = 0
total = 0
for row in range(first_sheet.nrows): #looking at all
    if str(first_sheet.cell(row,0).value) == 'Thursday':
        i = i + 1
        total = total + (first_sheet.cell(row,1).value)
        print("total i is now", i)
        print('total sales is now', total)
        plt.plot(i, total, 'o', color = 'purple')
    else:
        pass
averagethu = total / i
print('Thursday Average is', averagethu)

i = 0
total = 0
for row in range(first_sheet.nrows): #looking at all
    if str(first_sheet.cell(row,0).value) == 'Friday':
        i = i + 1
        total = total + (first_sheet.cell(row,1).value)
        print("total i is now", i)
        print('total sales is now', total)
        plt.plot(i, total, 'o', color = 'green')
    else:
        pass
averagefri = total / i
print('Friday Average is', averagefri)

i = 0
total = 0
for row in range(first_sheet.nrows): #looking at all
    if str(first_sheet.cell(row,0).value) == 'Saturday':
        i = i + 1
        total = total + (first_sheet.cell(row,1).value)
        print("total i is now", i)
        print('total sales is now', total)
        plt.plot(i, total, 'o', color = 'yellow')
    else:
        pass

averagesat = total / i
print('Saturday Average is', averagesat)

i = 0
total = 0
for row in range(first_sheet.nrows): #looking at all
    if str(first_sheet.cell(row,0).value) == 'Sunday':
        i = i + 1
        total = total + (first_sheet.cell(row,1).value)
        print("total i is now", i)
        print('total sales is now', total)
        plt.plot(i, total, 'o', color = 'pink')
    else:
        pass
averagesun = total / i
print('Sunday Average is', averagesun)
plt.show()
totalavg = {averagemon: 'Monday', averagetue: 'Tuesday', averagewed: 'Wednesday', averagethu: 'Thursday', averagefri: 'Friday', averagesat: 'Saturday', averagesun: 'Sunday'}
print(totalavg)
max_value = max(totalavg)
print(str, max_value)