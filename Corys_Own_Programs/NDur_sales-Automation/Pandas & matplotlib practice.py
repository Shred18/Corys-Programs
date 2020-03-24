import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import xlrd
data = pd.read_excel('SalesAutomate.xlsx',skiprows=1) #THIS LETS YOU SKIP THE FIRST ROW, WHICH WAS CAUSING SO MANY FUCKING PROBLEMS
#pd.set_option('display.max_columns',20)
#pd.set_option('display.max_rows',400)
data.head()

#couple_columns = data[['Date','Sold','Revenue']]

data.plot.scatter(x='Date',y='Revenue')

#sns.regplot(x='Date',y='Revenue',data=data)