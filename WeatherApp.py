from tkinter import *
import requests

root=Tk() 
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable()

def get(city):
    api="79de5817a4d223b536ce61a0f630a4b4"
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'appid':api, 'q':city, 'units':'Metric'}
    response=requests.get(url,params=params)
    report=response.json()
    
    label['text']=show(report)


def show(report):
    try:
        city= report['name']
        weather_condition= report['weather'][0]['description']
        temp= report['main']['temp']
        pressure = report['main']['pressure']
        humidity = report['main']['humidity']
        wind = report['wind']['speed']
        output= 'City: %s \nCondition: %s \nTemperature(°C): %s \n Pressure: %s  \n Humidity: %s \n wind: %s' %(city,weather_condition,temp,pressure,humidity,wind)
    except:
        output='Problem in show weather function'
    return output


image_icon=PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

 #logo
Logo_image=PhotoImage(file="logo2.png")
logo=Label(image=Logo_image)
logo.place(x=30,y=30)

canvas=Canvas(root,width=666,height=666)
canvas.pack()



frame=Frame(root,bd=1,bg='black')
frame.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.7,anchor='n')

entry=Entry(frame,font=('Helvetica',20),fg='white',bg='#6e8084')
entry.place(relheight=1,relwidth=0.7)

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(frame,image=Search_icon,borderwidth=0,cursor="hand2",bg="lightblue",command=lambda: get(entry.get()))
myimage_icon.place(relx=0.7,relheight=1,relwidth=0.3)



low_frame=Frame(root,bd=1)
low_frame.place(relx=0.5,rely=0.3,relheight=0.6,relwidth=.75,anchor='n')


label=Label(low_frame,font=('Helvectica',20),justify='center',bd=4,)
label.config(font=40,bg='white')
label.place(relheight=1,relwidth=1)


root.mainloop()