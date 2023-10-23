import pyttsx3
import webbrowser
import smtplib
import random
#import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import turtle
from matplotlib import pyplot as plt
import datetime


engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('2A5K7W-T3AU236GTR')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Edith: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning! ')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello akshat, I am Edith!')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))
    myCommand()

    return query
    
def history():
    file=open('history.txt','a')
    write=query
    file.write(write+'\n')
    file.close()
    


if __name__ == '__main__':

    while True:
    
        query = input('enter : ')
        query = query.lower()
        history()
        
        if 'open youtube' in query:
            speak('what would you like to watch , sir ?')
            video_name=input('search:')
            speak('okay')
            webbrowser.open('www.youtube.com/results?search_query='+video_name)

        elif 'open google' in query:
            speak('what would you like to search for, sir ?')
            google_search=input('search:')
            speak('okay')
            webbrowser.open(google_search)

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = input('enter the recipient')

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = input('Enter the content')
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("akshatchaube22@gmail.com", 'akki')
                    server.sendmail('akshatchaube22@gmail.com', "akshatchaube11@gmail.com", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello'  in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit() 
            
        elif 'who is akshat' in query:
            speak('He is my creator ')
        
        elif 'who are you' in query:
            speak('My name is Edith, i am Akshat\'s personal assistant and friend.')
        
        elif 'are you a girl' in query:
            speak('I am just a program, with a girl\'s voice, that\'s it.')
         
        elif 'who made you' in query:
            speak('Akshat Chaube brought me to life ! ')
            
        elif 'self destruct' in query:
            
            t=turtle.Turtle()
            t.getscreen().bgcolor("black")
            t.pencolor("red")
            a=0
            b=0
            t.speed(0)
            t.penup()
            t.goto(0,200)
            t.pendown()
            while True:
                t.forward(a)
                t.right(b)
                a+=3
                b+=1
                if b==210:
                    break
                    t.hideturtle()
            speak('boom  ! boom  ! boom !  !!!')
            sys.exit()
            
        elif 'open the bank' in query:
        
            date=datetime.date.today()
            print("")
            print("                  *********** BANK TRANSACTION SYSTEM ***********")
            print("                      Brought to you by : Class 12 python group ")
            
            speak(" Select an option (1 to 10):-")
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
            input()
            while(True):
                print('**********************')
                print('')
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
                    speak("All information prompted are mandatory to be filled")
                    acno=str(input("Enter account number:"))
                    name=input("Enter name(limit 35 characters):")
                    city=str(input("Enter city name:"))
                    mn=str(input("Enter mobile no:"))
                    balance=0
                    mycursor.execute("insert into details values('"+acno+"','"+name+"','"+city+"','"+mn+"','"+str(balance)+"')")
                    mydb.commit()
                    speak("Account successfully created !!!")
                    
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
                    speak("money has been deposited successfully!!!")
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
                    speak('Money has been withdrawn successfully!')

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
                        speak('The name has been updated.')
                    elif option=='2':
                        city=input('enter your new city name : ')
                        mycursor.execute("update details set city='"+city+"'where acno="+acno+"")
                        speak('The city has been updated.')
                    elif option=='3':
                        mn=input('enter your new mobileno : ')
                        mycursor.execute("update details set mobileno='"+mn+"'where acno="+acno+"")
                        speak('The mobile number has been updated.')
                    else:
                        speak('Choose correct option next time.')
                        pass
                    mydb.commit()        
                elif(ch==9):
                        
                        acno=input('Enter the account number:')
                        confirmation=input("Are you sure you want to delete all the data of the account.(Y/N)")
                        if confirmation=='Y': 
                            mycursor.execute("delete from transactions where acno="+acno+"")
                            mycursor.execute("delete from details where acno="+acno+"")
                            speak("account has been closed successfully")
                            mydb.commit()
                        elif confirmation=='N':
                            speak('Ok ! We\'ll head back to the menu.')
                        
                else:
                    break
                    
        
           
        elif query=='note':
            file=open('note.txt','a')
            write=input('Write down :')
            file.write(write+'\n')
            file.close()
            
        elif query=='show note':
            file=open('note.txt','r+')
            data=file.readlines()
            
            for i in data:
                print('')
                print(i,sep='\t',end='\n') 
                
        elif 'play a song' in query:
            music_folder='C:\\Users\\satis\\OneDrive\\Desktop\\Python\\Edith\\songs\\'
            music = ['1','2']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music! Enjoy!')
            
        elif query=='set timer':
            timer(words,sec)
        
        else:
            query = query
            speak('Hold on, let me check sir')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak(results)
        
            except:
                try: 
                    from googlesearch import search 
                except ImportError:  
                    print("No module named 'google' found")
  
                for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
                    print(j) 
                    webbrowser.open(j)
               # webbrowser.open('www.google.com')
        print('')
        speak('Anything else I can help you with , sir ?')
        


        
