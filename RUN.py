# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 11:39:10 2023

@author: Simran-pc
"""

from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
import pickle
import pandas as pd
import numpy as np


root = Tk()
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+-9+0')
root.title("Registration Form")
root.configure(background="white")

model=pickle.load(open('LinearRegressionModel.pkl','rb'))
car=pd.read_csv('Cleaned_data.csv')
print("file opend ")

companies=sorted(car['company'].unique())
car_models=sorted(car['name'].unique())
year=sorted(car['year'].unique(),reverse=True)
fuel_type=car['fuel_type'].unique()


COMP=StringVar()
MODEL=StringVar()
FUEL=StringVar()
YEAR=StringVar()
MODEL=StringVar()
km=tk.StringVar()
a=tk.StringVar()
def predict():
   
    #print(MODEL,COMP,YEAR)
    prediction=model.predict(pd.DataFrame(columns=['MODEL', 'COMP', 'YEAR', 'KM', 'FUEL'],
                              data=np.array([car_model,company,year,driven,fuel_type]).reshape(1, 5)))
    
    print(prediction)


app_width=700
app_height=600
xcor=(root.winfo_screenwidth()/2)-(app_width/2)
ycor=(root.winfo_screenheight()/2)-(app_height/2)
frame1=Frame(root,bg="red")
frame1.place(x=xcor,y=ycor,width=700,height=800)
l1 = Label(frame1, text="ENTER CAR DETAILS HERE",font=("times new roman",20,"bold"),bg='white',fg='green')
l1.place(x=150,y=20)
l2 = Label(frame1, text="COMPANY",font=("times new roman",15,"bold"),bg='white',fg='gray')
l2.place(x=90,y=80)
e1 = Entry(frame1,font=("times new roman",15),textvariable=COMP,bg='lightgray')
e1.place(x=90,y=120,width=520)
l4 = Label(frame1, text="ENTER MODEL",font=("times new roman",15,"bold"),bg='white',fg='gray')
l4.place(x=90,y=170)
e3 = Entry(frame1,font=("times new roman",15),textvariable=MODEL,bg='lightgray')
e3.place(x=90,y=210,width=520)
l6 = Label(frame1, text="YEAR OF PURCHASE",  font=("times new roman",15,"bold"),bg='white',fg='gray')
l6.place(x=90,y=250)
e4 = Entry(frame1,font=("times new roman",15),textvariable=YEAR,bg='lightgray')
e4.place(x=90,y=300,width=520)
l7 = Label(frame1, text="FUEL TYPE",  font=("times new roman",15,"bold"),bg='white',fg='gray')
l7.place(x=90,y=340)
e5 = Entry(frame1,font=("times new roman",15),textvariable = FUEL,bg='lightgray')
e5.place(x=90,y=380,width=520)
l8 = Label(frame1, text="KM DRIVEN",  font=("times new roman",15,"bold"),bg='white',fg='gray')
l8.place(x=90,y=420)
e5 = Entry(frame1,font=("times new roman",15),textvariable=km,bg='lightgray')
e5.place(x=90,y=460,width=520)
a=km.get()
print(a)

b1 = Button(frame1, text='PREDICT VALUE',width=20,command="predict",bg='green',fg='white',font=("times new roman",15,"bold"))
b1.place(x=200,y=500)

#print(MODEL,COMP,YEAR)







root.mainloop()

