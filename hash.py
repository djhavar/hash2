from tkinter import *
from firebase import firebase
from simplecrypt import encrypt,decrypt

login_window = Tk()
login_window.geometry("400x400")
login_window.config(bg='#AB92BF')

user=''
code=''
fcode=''
messt=''
messe=''

def sendData():
    global user
    global messe
    global code
    
    message = user+":"+messe.get()
    ciphercode=encrypt('AIM',message)
    hex_string = ciphercode.hex()
    put_date = firebase.put("/",your_code,hex_string)
    print(put_date)
    
def enterRoom():
    global user
    global messe
    global code
    global fcode
    global messt
    
    code = code.get()
    fcode = fcode.get()
    user = user.get()
    login_window.destroy()
    

    message_window= Tk()
    message_window .geometry("399x400")
    message_window .config(bg='#AB92BF')
    
    messaget=Text(message_window,height=20,width=70)
    messaget.place(relx=0.5,rely=0.35,anchor=CENTER)
    
    messageL=Label(message_window,text="message",height=20,width=70,fg="white",font="arial")
    messaget.place(relx=0.3,rely=0.8,anchor=CENTER)
    
    messageE=Entry(message_window, font='arial 15')
    messaget.place(relx=0.6,rely=0.8,anchor=CENTER)