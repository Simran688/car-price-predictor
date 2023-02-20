# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 19:03:44 2023

@author: Simran-pc
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 14:23:41 2022

@author: Simran-pc
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pickle
import pandas as pd
import numpy as np
from ttkwidgets.autocomplete import AutocompleteEntry


model=pickle.load(open('LinearRegressionModel.pkl','rb'))
car=pd.read_csv('Cleaned_data.csv')
companies=sorted(car['company'].unique())
car_models=sorted(car['name'].unique())
year=sorted(car['year'].unique(),reverse=True)
fuel_type=car['fuel_type'].unique()



root = Tk()
root.configure(bg='white')
frame_header=Frame(root,bg='white')
frame_header.pack()

#logo = PhotoImage(file='logo.png').subsample(2, 2)
#logolabel = ttk.Label(frame_header, text='logo',background='white', image=logo)
#logolabel.grid(row=0, column=0)
headerlabel = ttk.Label(frame_header, text='''             BHAI PARMANAD DSEU CAMPUS ''', foreground='red',background='white',font=('arial', 36,'bold'))
headerlabel.grid(row=0,column=1)
headerlabel1 = ttk.Label(frame_header, text='''       CAR PRICE PREDICTOR         ''', foreground='black',background='white',font=('arial', 24,'bold'))
headerlabel1.grid(row=1,column=1,pady=10)
messagelabel = ttk.Label(frame_header,text='FILL THE INFORMATION ABOUT CAR',background='white',foreground='purple', font=('Arial', 10))
messagelabel.grid(row=2, column=1)

frame_content =Frame(root,bg='white')
frame_content.pack()


# def submit():
#     username = entry_name.get()
#     print(username)

company = StringVar()
var = StringVar()
reg=StringVar()
ph=StringVar()
cour=StringVar()
dep=StringVar()

Checkbutton1 = IntVar()  
Checkbutton2 = IntVar()  
Checkbutton3 = IntVar()
# cmnt= StringVar()
namelabel = ttk.Label(frame_content, text='ENTER COMPANY NAME:',font=('arial',10,'bold'),background='white',)
namelabel.grid(row=0, column=0,columnspan=2,padx=5, pady=10,sticky='sw')
enterycompany=ttk.Entry(frame_content,width=20, textvariable =company)
#enterycompany=AutocompleteEntry(frame_content,completevalues=companies)
#entry_name = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=myvar,background='white',foreground='black')
entrycompany.grid(row=0, column=1,columnspan=2,padx=5,pady=10,sticky='sw')
#enterycompany.pack()
#entry_name.AutocompleteEntry(frame_content,completevalues=countries)



#GENDER
gender=StringVar()
gender.set(3)
genderlabel=ttk.Label(frame_content, text='GENDER:',font=('arial',10,'bold'),background='white')
genderlabel.grid(row=1,column=0,columnspan=3, padx=5,pady=10,sticky='sw')
radiobutton=Radiobutton(frame_content,text='MALE',variable=gender,value='MALE',font=("arial",10),background='white')
radiobutton.select()
radiobutton.grid(row=1,column=1, pady=10,sticky='sw')
radiobutton1=Radiobutton(frame_content,text='FEMALE',variable=gender,value='FEMALE',font=("arial",10),background='white')
radiobutton1.deselect()
radiobutton1.place(x=210,y=58)
radiobutton2=Radiobutton(frame_content,text='OTHERS',variable=gender,value='OTHERS',font=("arial",10),background='white')
radiobutton2.deselect()
radiobutton2.place(x=315,y=58)

#COURSE
courselabel=ttk.Label(frame_content, text='COURSE:',font=('arial',10,'bold'),background='white')
courselabel.grid(row=2,column=0,columnspan=5,padx=5, pady=10,sticky='sw')
options=['B.E',
         'B.Tech',
         'M.E',
         'M.Tech',
         'MBA']
combobutton=ttk.Combobox(frame_content,textvariable=cour,width=30,value=options,background='blue')
combobutton.grid(row=2,column=1,columnspan=5,padx=5,pady=10,sticky='sw')

#DEPARTMENT
departmentlabel=ttk.Label(frame_content, text='DEPARTMENT:',font=('arial',10,'bold'),background='white')
departmentlabel.grid(row=2,column=2,columnspan=2,padx=5, pady=10,sticky='sw')
options1=['Computer Science And Engineering',
          'Electrical And Electronic Engineering',
          'Mechanical Engineering',
          'Electrical And Instrument Engineering',
          'Information Technology',
          'Electrical And Communication Engineering',
          'Civil Engineering',
          'Automobile Engineering']        
combobutton1=ttk.Combobox(frame_content,textvariable=dep,width=30,value=options1,background='white')
combobutton1.grid(row=2,column=3,columnspan=2,padx=5,pady=10,sticky='sw')

#RESIGTER NO
registernolabel = ttk.Label(frame_content, text='REGISTER NO. :',background='white', font=('Arial', 10,'bold'))
registernolabel.grid(row=3, column=0, padx=5,pady=10,sticky='sw')
entry_registerno = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=reg,background='white')
entry_registerno.grid(row=3, column=1,columnspan=2,padx=5,pady=10,sticky='sw')

# PHONE NUMBER
phnumberlabel = ttk.Label(frame_content, text='PHONE NUMBER:', font=('Arial', 10,'bold'),background='white')
phnumberlabel.grid(row=4, column=0, padx=5,pady=10,sticky='sw')
entry_phnumber = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=ph,background='white')
entry_phnumber.grid(row=4, column=1,columnspan=2,padx=5,pady=10,sticky='sw')


#EMAIL ID
emaillabel = ttk.Label(frame_content, text='EAMIL:', font=('Arial', 10,'bold'),background='white')
emaillabel.grid(row=5, column=0, padx=5,pady=10,sticky='sw')
entry_email = ttk.Entry(frame_content, width=18, font=('Arial', 14), textvariable=var,background='white')
entry_email.grid(row=5, column=1,columnspan=2,padx=5,pady=10,sticky='sw')

#COMMENT
commentlabel = ttk.Label(frame_content, text='COMMENT:', font=('Arial', 10,'bold'),background='white')
commentlabel.place(x=5,y=340)
textcomment = Text(frame_content, width=45, height=8,background='white')
textcomment.grid(row=6, column=1, padx=5,pady=10,columnspan=2)
textcomment.config(wrap ='word')
# def clear():
#     textcomment.delete(1.0,'end')
def clear():
    global entry_name
    global entry_email
    global textcomment
    global entry_phnumber
    global entry_registerno
    global combobutton1
    global combobutton
    global radiobutton
    global radiobutton1
    global radiobutton2
    messagebox.showinfo(title='clear', message='Do you want to clear?')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)
    entry_phnumber.delete(0, END)
    entry_registerno.delete(0, END)
    combobutton1.delete(0, END)
    combobutton.delete(0, END)
    radiobutton.select()
    radiobutton1.deselect()
    radiobutton2.deselect()


def submit():
    global entry_name
    global entry_email
    global textcomment
    global entry_phnumber
    global entry_registerno
    global combobutton1
    global combobutton
    global radiobutton
    global radiobutton1
    global radiobutton2
    print('Name:',myvar.get())
    print('Gender:',gender.get())
    print('course:',cour.get())
    print('Department:',dep.get())
    print('Register number:',reg.get())
    print('Phone number:',ph.get())
    print('Email:',var.get())
    print('Comment:',textcomment.get(1.0, END))
    messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)
    entry_phnumber.delete(0, END)
    entry_registerno.delete(0, END)
    combobutton1.delete(0, END)
    combobutton.delete(0, END)
    radiobutton.select()
    radiobutton1.deselect()
    radiobutton2.deselect()



submitbutton = ttk.Button(frame_content, text='Submit', command=submit).grid(row=7, column=0, sticky='e')
clearbutton = ttk.Button(frame_content, text='Clear', command=clear).grid(row=7, column=1, sticky='w')

mainloop()