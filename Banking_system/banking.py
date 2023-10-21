#SOURCE CODE FOR BANKING TRANSACTIONS
from matplotlib import pyplot as plt 
import datetime
import sys
date=datetime.date.today()
print("")
print("                  *********** BANK TRANSACTION SYSTEM ***********")
print("                      Brought to you by : Akshat Chaube ")
print("********************************************************************************************")
input()
print(" Select an option (1 to 10):-")
#creating database
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Tiger")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists banking")
mycursor.execute("use banking")
#creating required tables
mycursor.execute("create table if not exists details(acno char(4) primary key,name varchar(30),city char(20),mobileno char(10),balance int(6))")
mycursor.execute("create table if not exists transactions(acno char (4),amount int(6),dot date,ttype char(1),foreign key (acno) references details(acno))")
mydb.commit()
while(True):
    print('**********************')
    input()
    print("  1=Create account")
    print("  2=Deposit money")
    print("  3=Withdraw money")
    print("  4=Display account")
    print("  5=Show graph")
    print("  6=Show pie chart")
    print("  7=Show scattered graph")
    print("  8=To update data")
    print("  9=close an account")
    print("  10=exit")
    ch=int(input("Enter your choice:"))
    
#PROCEDURE FOR CREATING A NEW ACCOUNT OF THE APPLICANT
    if(ch==1):
        print("All information prompted are mandatory to be filled")
        acno=str(input("Enter account number:"))
        name=input("Enter name(limit 35 characters):")
        city=str(input("Enter city name:"))
        mn=str(input("Enter mobile no:"))
        balance=0
        mycursor.execute("insert into details values('"+acno+"','"+name+"','"+city+"','"+mn+"','"+str(balance)+"')")
        mydb.commit()
        print("Account successfully created !!!")
        
#PROCEDURE FOR UPDATING DETAILS AFTER THE DEPOSITION OF MONEY BY THE APPLICANT
    elif(ch==2):
        acno=str(input("Enter account number:"))
        dp=int(input("Enter amount to be deposited:"))
        dot=str(date)
        print('date of transaction is recorded as:',dot)
        ttype="d"
        mycursor.execute("insert into transactions values('"+acno+"','"+str(dp)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update details set balance=balance+'"+str(dp)+"' where acno='"+acno+"'")
        mydb.commit()
        print("money has been deposited successully!!!")
#PROCEDURE FOR UPDATING THE DETAILS OF ACCOUNT AFTER THE WITHDRAWL OF MONEY BY THE APPLICANT

    elif(ch==3):
        acno=str(input("Enter account number:"))
        wd=int(input("Enter amount to be withdrawn:"))
        dot=str(date)
        print('date of transaction is recorded as:',dot)
        ttype="w"
        mycursor.execute("insert into transactions values('"+acno+"','"+str(wd)+"','"+dot+"','"+ttype+"')")
        mycursor.execute("update details set balance=balance-'"+str(wd)+"' where acno='"+acno+"'")
        mydb.commit()
        print('Money has been withdrawn successully!')

#PROCEDURE FOR DISPLAYING THE ACCOUNT OF THE ACCOUNT HOLDER AFTER HE/SHE ENTERS HIS/HER ACCOUNT NUMBER
    elif(ch==4):
        acno=str(input("Enter account number:"))
        mycursor.execute("select * from details where acno='"+acno+"'")
        for i in mycursor:
            print(i)
#PROCEDURE TO CREATE A LINE GRAPH USING MATPLOTLIB
    elif(ch==5):
            x=mycursor.execute("select name from details")
            names=[]
            for j in mycursor:
                names+=j
            print('names = ',names)
            y=mycursor.execute("select balance from details")
            balance=[]
            for k in mycursor:
                balance+=k
            print('balance = ',balance)
            
            plt.plot(names,balance,label='Account Balance')
            plt.xticks(names,names, rotation=30)
            plt.title('Account balance of account holders.')
            plt.ylabel('bank balance.')
            plt.xlabel('Names of account holders.')
            plt.legend()
            plt.show()
#PROCEDURE TO CREATE A PIE CHART USING MATPLOTLIB
    elif(ch==6):
            x=mycursor.execute("select name from details")
            names=[]
            for j in mycursor:
                names+=j
            print('names = ',names)
            y=mycursor.execute("select balance from details")
            balance=[]
            for k in mycursor:
                balance+=k
            print('balance = ',balance)
            plt.pie(balance,explode=None,labels=names,colors=None)
            plt.title("Grouping of all the bank holders")
            plt.show()
    elif(ch==7):
            x=mycursor.execute("select name from details")
            names=[]
            for j in mycursor:
                names+=j
            print('names = ',names)
            y=mycursor.execute("select balance from details")
            balance=[]
            for k in mycursor:
                balance+=k
            print('balance = ',balance)
            plt.scatter(names,balance,alpha=0.9)
            plt.title("Grouping of all the bank holders in scattered graph")
            plt.xlabel('names of the bank account holders')
            plt.ylabel('balance')
            plt.show()
            
#PROCEDURE TO UPDATE THE DATA IN THE TABLE    
    elif(ch==8):
        
        acno=input('enter your account number : ')
        print('Select your choice (1 to 3):')
        print("1= Name")
        print("2= City")
        print("3= Mobileno")
        option=input("What would you like to update : ")
        
        if option=='1':
            name=input('enter your new name : ')
            mycursor.execute("update details set name='"+name+"'where acno="+acno+"")
            print('The name has been updated.')
        elif option=='2':
            city=input('enter your new city name : ')
            mycursor.execute("update details set city='"+city+"'where acno="+acno+"")
            print('The city has been updated.')
        elif option=='3':
            mn=input('enter your new mobileno : ')
            mycursor.execute("update details set mobileno='"+mn+"'where acno="+acno+"")
            print('The mobile number has been updated.')
        else:
            print('Choose correct option next time.')
            pass
        mydb.commit()        
    elif(ch==9):
            
            acno=input('Enter the account number:')
            confirmation=input("Are you sure you want to delete all the data of the account.(Y/N)")
            if confirmation=='Y': 
                mycursor.execute("delete from transactions where acno="+acno+"")
                mycursor.execute("delete from details where acno="+acno+"")
                print("account has been closed successfully")
                mydb.commit()
            elif confirmation=='N':
                print('Ok ! We\'ll head back to the menu.')
            else:
                print('Try again later')
                pass
    else:
        sys.exit()
