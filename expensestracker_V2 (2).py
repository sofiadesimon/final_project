import numpy as np
import pandas as pd
from datetime import date

#create empty list
GOODS_OR_SERVICES_LIST = []  
PRICES_LIST =[] 
DATES_LIST = []
EXPENSE_TYPE_LIST = []

#create a function to add the expense to the lists and organize the data
def add_expense ( GOODS_OR_SERVICES, PRICES, DATES, EXPENSE_TYPE):
  GOODS_OR_SERVICES_LIST.append (GOODS_OR_SERVICES)
  PRICES_LIST.append (PRICES)
  DATES_LIST.append (DATES)
  EXPENSE_TYPE_LIST.append (EXPENSE_TYPE)

#convert lists into a single list
REPORT = []
REPORT.append (GOODS_OR_SERVICES_LIST)
REPORT.append (PRICES_LIST)
REPORT.append (DATES_LIST)
REPORT.append (EXPENSE_TYPE_LIST)

#Main program 
option = -1 #this is a variable that shows the user option or choice or input
while (option != 0):
    #create the option menu
    print("welcome to the simple expense tracker")
    print("1. Add Grocery expense") #this is the first option
    print("2. Add Household expense") #this is the second option
    print("3. Add Pharmacy expense") #this is the third option
    print("4. Add Beauty expense") #this is the third option
    print("5. Show And Save The Expense Report") #this is the fifth option
    print("0. exit") #this is the last option to exit the programm (menu)
    option = int(input("Choose an option:\n")) #here the integer is put because the user will input a number for the choice (1 to 4 as shown above)
    
#then I want to print a new line
    print ()

#Check for the user choice or option or input 
    if option == 0:
        print ("Go out of the main menu")
        break

    elif option == 1:
        print ("Adding Grocery")
        EXPENSE_TYPE="Grocery"
    elif option == 2:
        print ("Adding Household")
        EXPENSE_TYPE="Household"
    elif option == 3:
        print ("Adding Pharmacy")
        EXPENSE_TYPE="Pharmacy"
    elif option == 4:
        print ("Adding Beauty")
        EXPENSE_TYPE="Beauty"
   
    elif option == 5:
        print ("Show And Save The Expense Report")  
        #here we want to save the expense report so we need to create a dataframe and then ADD all the expenses
        REPORT_df= pd.DataFrame(REPORT).transpose()
        REPORT_df.columns=["option", "price","date","expense type"]
     
        #THEN I need to save this report in csv format 
        REPORT_df.to_csv("expenses.csv")
        
        #Then I also want to ofc display this report 
        print(REPORT_df)
        
    else: #this is the optiion in case the user picks an incorrect (so no existence option)
        print("Man You chose an incorrect option, you can choose either 0,1,2,3,4 or 5, otherwise you do not get anything out of this")
            
        #Allow the user to enter the good or services and the price
    if (option !=-1):
            GOODS_OR_SERVICES = str(input("Enter the good or services for the expense type"+"="+ EXPENSE_TYPE+ "=")),
            PRICES = (input("Enter the price of the good or service"+ "=")), #it is a float cause prices are not alwazys integer 
            today = date.today(), #add from date packages the date of today automatically
            add_expense(GOODS_OR_SERVICES, PRICES, today, EXPENSE_TYPE)
    
    else:
        print()
        
#print a new line 
print()
    
    
    
    


