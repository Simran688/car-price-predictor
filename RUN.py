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
root.title("Car Price Prediction")
root.configure(background="#f0f0f5")

# Load model and data
model = pickle.load(open('LinearRegressionModelfinal.pkl', 'rb'))
car = pd.read_csv('Cleaned_data.csv')


companies = sorted(car['company'].unique())
car_models = sorted(car['name'].unique())
years = sorted(car['year'].unique(), reverse=True)

# Variables to store user input
COMP = StringVar()
MODEL = StringVar()
FUEL = StringVar()
YEAR = StringVar()
KM = StringVar()

# Fuel Type Checkboxes
fuel_types = ["Petrol", "Diesel", "LPG"]
fuel_checkboxes = {}

def validate_fields():
    """Validates all input fields."""
    # Basic checks for string fields
    def is_valid_string(value):
        return 2 <= len(value) <= 15

    try:
        # Validate required string fields
        company = COMP.get().strip()
        car_model = MODEL.get().strip()
        if not (is_valid_string(company) and is_valid_string(car_model)):
            raise ValueError("Company and Car Model must be between 2 to 15 characters.")

        # Validate year and kilometers driven
        year = int(YEAR.get())
        driven = int(KM.get())
        if year < 1900 or driven <= 0:
            raise ValueError("Enter a valid Year and positive Kilometers driven.")

        # Ensure only one fuel type checkbox is selected
        selected_fuels = [fuel for fuel, var in fuel_checkboxes.items() if var.get()]
        if len(selected_fuels) != 1:
            raise ValueError("Please select exactly one fuel type.")

        return company, car_model, year, driven, selected_fuels[0]

    except ValueError as ve:
        mb.showerror("Input Error", str(ve))
        return None

def predict():
    validated_data = validate_fields()
    if not validated_data:
        return

    company, car_model, year, driven, fuel_type = validated_data

    try:
        prediction_input = pd.DataFrame(
            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
            data=np.array([car_model, company, year, driven, fuel_type]).reshape(1, 5)
        )

        # Make the prediction
        prediction = model.predict(prediction_input)
        mb.showinfo("Prediction", f"Predicted Car Price: ₹{prediction[0]:,.2f}")

    except Exception as e:
        mb.showerror("Error", f"Prediction failed: {str(e)}")

# UI Improvements
app_width, app_height = 700, 600
xcor = (root.winfo_screenwidth() / 2) - (app_width / 2)
ycor = (root.winfo_screenheight() / 2) - (app_height / 2)

frame1 = Frame(root, bg="#ffffff", highlightbackground="#000000", highlightthickness=2)
frame1.place(x=xcor, y=ycor, width=700, height=700)

l1 = Label(frame1, text="Car Price Prediction", font=("Arial", 24, "bold"), bg='white', fg='#4CAF50')
l1.place(x=180, y=20)

def create_label_entry(frame, text, var, y_offset):
    label = Label(frame, text=text, font=("Arial", 14, "bold"), bg='white', fg='gray')
    label.place(x=90, y=y_offset)
    entry = Entry(frame, font=("Arial", 14), textvariable=var, bg='lightgray')
    entry.place(x=90, y=y_offset + 40, width=520)

create_label_entry(frame1, "Company", COMP, 80)
create_label_entry(frame1, "Car Model", MODEL, 170)
create_label_entry(frame1, "Year of Purchase", YEAR, 260)
create_label_entry(frame1, "Kilometers Driven", KM, 350)

# Fuel Type Checkboxes
fuel_label = Label(frame1, text="Fuel Type", font=("Arial", 14, "bold"), bg='white', fg='gray')
fuel_label.place(x=90, y=440)

fuel_frame = Frame(frame1, bg="white")
fuel_frame.place(x=90, y=480)

# Logic to ensure only one checkbox is selected at a time
def on_fuel_checkbox_selected(selected_fuel):
    for fuel, var in fuel_checkboxes.items():
        if fuel != selected_fuel:
            var.set(0)

for i, fuel in enumerate(fuel_types):
    var = IntVar()
    fuel_checkboxes[fuel] = var
    checkbox = Checkbutton(
        fuel_frame, text=fuel, variable=var, font=("Arial", 12), bg='white',
        command=lambda f=fuel: on_fuel_checkbox_selected(f)
    )
    checkbox.grid(row=0, column=i, padx=10)

# Predict Button
b1 = Button(frame1, text='Predict Value', width=20, command=predict,
            bg='#4CAF50', fg='white', font=("Arial", 15, "bold"))
b1.place(x=250, y=550)

root.mainloop()
