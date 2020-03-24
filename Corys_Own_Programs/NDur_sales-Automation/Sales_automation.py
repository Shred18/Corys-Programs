#This is a program that is linked to your excel sheet, and will update with the sheet, It will allow you to calculate the amount of taxes you owe based off profit,
#the amount you've profited to date by week,
#your expenses by week,
#the platform that is selling the best


import xlrd
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

Excelsheet = 'SalesAutomate.xlsx'
book = xlrd.open_workbook(Excelsheet)

sales = pd.read_excel('SalesAutomate.xlsx')
#desired_width = 320 #set the desired width
#pd.set_option('display.width',desired_width) #sets to this increased width
#pd.set_option('display.max_columns', 60) #spreads width out to 10 columns
#pd.set_option('display.max_rows', 400)


#plt.plot(revenue, profit())


first_sheet = book.sheet_by_index(0) #telling python to just look at the first sheet - I think this may be required
second_sheet = book.sheet_by_index(1) #telling python to look at the second sheet
#print(first_sheet.row_values(1)) #when looking in the first sheet, this is telling python to look at strictly the second row. Problem comes up when

headings = first_sheet.row_values(1) #setting this to the heading

firstseven = headings[0:7] #prints only the first 6 headings for the second column in this program
#print(firstseven)






def revenue():

    sheet = first_sheet
    totalrev = 0.0
    for row in range(sheet.nrows): #looking in nrows for the sheet entirely
        data = sheet.cell_value(row,5) #looking at specifically the revenue column, iterating through it. setting it equal to variable
        if row > 1:
            totalrev += data
            #print(totalrev)
        else:
            continue
    return(totalrev)





def invexpenses():
    sheet = first_sheet
    exp = 0
    for row in range(sheet.nrows):

        if sheet.cell(row,4).value == 1:
            exp += 15
        elif sheet.cell(row,4).value == 2:
            exp += 30
        elif sheet.cell(row,4).value == 3:
            exp +=45
        elif sheet.cell(row,4).value == 4:
            exp += 60
        elif sheet.cell(row,4).value == 5:
            exp += 75
        elif sheet.cell(row,4).value == 6:
            exp += 90
        elif sheet.cell(row,4).value == 7:
            exp += 105
        elif sheet.cell(row,4).value == 8:
            exp += 120
        elif sheet.cell(row,4).value == 9:
            exp += 135
        elif sheet.cell(row,4).value == 10:
            exp += 150
        else:
            continue
    return(exp)


def grossprofit():
    x = revenue() #passing the function in - this is a must if you'd like to use it in another function
    y = invexpenses()
    return(x - y)

def taxes():
    x = grossprofit()
    if x >= 0:
        tax = .153
        taxprice = x * tax
        return(taxprice)
    else:
        print('you didnt make a profit, so youre not taxed')

def profit():
    x = grossprofit()
    y = taxes()
    if x >= 0:
        return(x - y)
    else:
        pass

#def pos():
   # sheet = first_sheet
    #mercari = 0
   # offerup = 0
   # facebook = 0
    #letgo = 0
   # for row in range(sheet.nrows):
    #    pos = sheet.cell_value(row,6)
     #   pos = pos.lower()
      #  if pos == 'mercari':
         #   mercari += 1
       # elif pos == 'offerup':
        #    offerup += 1
       # elif pos == 'facebook':
          #  facebook += 1
       # elif pos == 'letgo':
        #    letgo += 1
        #else:
         #   pass
    #print('Mercari sales', mercari, 'Offerup sales', offerup, 'Facebook sales', facebook, 'Letgo sales', letgo)
   #return(mercari, offerup, facebook, letgo)


def pospercent():
    sheet = first_sheet
    mercari = 0
    offerup = 0
    facebook = 0
    letgo = 0
    for row in range(sheet.nrows):
        sold = sheet.cell_value(row,4)
        pos = sheet.cell_value(row, 6)
        pos = pos.lower()
        if row > 1 and pos == 'mercari':
            mercari += sold
        elif row > 1 and pos == 'offerup':
            offerup += sold
        elif row > 1 and pos == 'facebook':
            facebook += sold
        elif row > 1 and pos == 'letgo':
            letgo += sold
        else:
            continue
    total = mercari + offerup + facebook + letgo
    mercaripercent = (mercari / total) * 100
    mercaripercent = round(mercaripercent,2)
    offeruppercent = (offerup / total) * 100
    offeruppercent = round(offeruppercent,2)
    facebookpercent = (facebook / total) * 100
    facebookpercent = round(facebookpercent,2)
    letgopercent = (letgo / total) * 100
    letgopercent = round(letgopercent,2)
   # print('Mercari sales', mercari, 'Offer Up sales', offerup, 'Facebook sales', facebook, 'Letgo sales', letgo)
    return(mercaripercent, offeruppercent, facebookpercent, letgopercent)

def busexp(): #expenses other than inventory
    sheet = second_sheet
    exp = 0
    for row in range(sheet.nrows):
        businessexp = sheet.cell_value(row,1)
        reason = sheet.cell_value(row,2)
        if row > 1:
            exp += businessexp
            #if reason != '': #instead of doing row, use reason. it's set to iterate through the entire "reason" column in excel
              #  print(reason) #prints the expense reasons if present
        else:
            continue
    return(exp)

def inventory():
    sheet = first_sheet
    print("Inventory Check:")
    for row in range(sheet.nrows):
        invname = sheet.cell_value(row, 9)
        invcount = sheet.cell_value(row,10)
        if invcount != '':
            inv = invcount
            name = invname
            #figure out how to use the list(map()) function, it will allow you to create a list when iterating through excel
            #so you dont have to print it & can return it instead
            print(name, inv)
        else:
            continue
    totalinv = 0
    for row in range(sheet.nrows):
        invcount = sheet.cell_value(row,10)
        if invcount != '':
            totalinv += invcount

        else:
            continue
    if totalinv < 25:
        print("ORDER INVENTORY, you're at:")
    return totalinv
       # return totalinv
def weeklysold():
    sheet = first_sheet
    theweek = -3
    weeklysalescount = 0
    weeklysales = []
    totalweeks = []



    for row in range(sheet.nrows):
        weeks = sheet.cell_value(row,0)
        sold = sheet.cell_value(row,4)
        if len(weeks) == 0:
            weeklysalescount += sold
            #print(theweek, weeklysales)
        else:
            weeklysales.append(weeklysalescount)
            totalweeks.append(theweek)
            theweek += 1
            weeklysalescount = sold
    return(totalweeks[3:], weeklysales[3:])

















