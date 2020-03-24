#Practice for automated bot to post on offer up for me

#TO RUN THIS, HIGHLIGHT ALL THE SCRIPT & HIT RUN IN PYTHON CONSOLE

def daily_time(time):

    if time > 1 and time < 12:
        print("We should make a post")
    else:
        print("go to fucking sleep")


#paying student loans program
def paying_loans(a,b):

    loans = 800
    #a is amount made
    #b is amount spent

    if a - b >= 0:
        print("you made enough to clear your loans you fuck")
    else:
        print("looks like u cant afford it hahahaha")





def products_sold_for_profit():

    a = 0
    revenue = a * 55
    total_sold = a * 15
    gross_profit = revenue - total_sold
    tax = gross_profit * .2
    after_tax_profit = gross_profit - tax
    goal = 100000



    while after_tax_profit < goal:
        a = a + 1
        revenue = a * 55
        total_sold = a * 15
        gross_profit = revenue - total_sold
        tax = gross_profit * .2
        after_tax_profit = gross_profit - tax

        print("you've sold ", a, "and have made", after_tax_profit)

    else:
        return after_tax_profit

    #This will tell you whether or not your business is profitable on a monthly basis, and by how much

def profitable_business():
    a = 1  # number of employees
    b = 0  # number of products sold
    employee_overhead = a * 3500
    prod_cost = b * 15
    revenue = b * 55
    gross_profit = revenue - prod_cost
    tax = gross_profit * .2
    real_profit = gross_profit - tax

    while real_profit < employee_overhead:
        a = 1
        b = b + 1
        employee_overhead = a * 3500
        prod_cost = b * 15
        revenue = b * 55
        gross_profit = revenue - prod_cost
        tax = gross_profit * .2
        real_profit = gross_profit - tax

        print("you're making ", real_profit, "while your employee overhead is", employee_overhead, "this took", b,
              "total units to do")

    else:
        print("you're profitable! you've made ", real_profit)






# how often one single number appears in a list (count only takes 1 argument)

def how_often():
    numbers = [1,2,3,4,3,3,4,5,4,4,5,3,5,4,6,7,5,3,2,2,3,4,66,6,5,3,2,1,3,1,1,2,4,6,3,3]


    count = numbers.count(1)

    print("number of times 1 appears is ", count)




def often_multiple():

    numbers = [1,2,3,4,5,4,3,2,3,4,5,6,7,7,7,6,5,4,5,6,7]

    for i in numbers:
        count = numbers.count(i)

        print(count)








