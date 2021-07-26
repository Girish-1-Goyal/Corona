from bs4 import BeautifulSoup as bs
import requests
import tkinter as tk
from tkinter import messagebox
import plyer
import threading
import time
import os


def refresh():
    new_data = get_data()
    lbl1['text'] = new_data

def exit():
    exit = tk.messagebox.askyesno('Exit','Do you want to really Exit')
    try:
        if exit is True:
            win.destroy()
        else:
            return
    except:
        return

def get_notification():
    while True:
        plyer.notification.notify(
            title="COVID-19 Report",
            message=get_data(),
            timeout=10,
            app_icon='2.ico'
        )
        time.sleep(30)
def get_time():
    time1 = time.asctime()
    return time1

def get_data():
    url = "https://www.mygov.in/covid-19"
    response = requests.get(url)
    data = bs(response.text,'html.parser')
    info = data.find('div',class_='information_row').find_all('div',class_='iblock_text')
    written_details = ''
    for block in info:
        numbers = block.find('span',class_='icount').get_text()
        text = block.find('div',class_='info_label').get_text()
        written_details +=  text + " : " + numbers+"\n"
    return written_details

win = tk.Tk()
win.title("COVID-19 Ananysis")
win.geometry("700x700+0+0")
win.resizable(width=False,height=False)
win.configure(background='#D5820F')

title = tk.Label(win,text='---COVID-19 Tracker---',font=('times new roman',30,"bold"))
title.pack(side='top',fill="x")
title.configure(background='yellow')

frm1 = tk.Frame(win,bd=9,relief='sunken',background="black")
frm1.place(x=30,y=50,width=630,height=400)

lbl1 = tk.Label(frm1,text=get_data(),background="black",foreground="white",font=('sans_serif',33))
lbl1.pack()

lbl2 = tk.Label(win,text=get_time(),foreground="black",background='#D5820F',font=('sans_serif',20))
lbl2.place(x=200,y=600)

btn1 = tk.Button(win,text='Refresh',width=20,height=2,command=refresh)
btn1.place(x=270,y=470)

btn2 = tk.Button(win,text='Exit',width=20,height=2,command=exit)
btn2.place(x=270,y=530)

th1 = threading.Thread(target=get_notification)
th1.setDaemon(True)
th1.start()

win.mainloop()
