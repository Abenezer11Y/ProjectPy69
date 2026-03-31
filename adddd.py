from tkinter import *
from datetime import date
import calendar

root = Tk()
root.title("Age Calculator App")
root.geometry('400x450')

def calculate():
    name = nam_entry.get()
    d = int(first_entry.get())
    m = int(sec_entry.get())
    y = int(thir_entry.get())
    
    today = date.today()
    age = today.year - y
    month_name = calendar.month_name[m]
    
    res_lbl.config(text=f"{name} is {age} years old.\nBorn in {month_name}")

nam_lbl = Label(text="Name", bg="#49eb51")
nam_lbl.pack()
nam_entry = Entry()
nam_entry.pack()

first_lbl = Label(text="Day", bg="#49eb51")
first_lbl.pack()
first_entry = Entry()
first_entry.pack()

sec_lbl = Label(text="Month", bg="#49eb51")
sec_lbl.pack()
sec_entry = Entry()
sec_entry.pack()

thir_lbl = Label(text="Year", bg="#49eb51")
thir_lbl.pack()
thir_entry = Entry()
thir_entry.pack()

btn = Button(text="Calculate", command=calculate)
btn.pack(pady=10)

res_lbl = Label(text="", font=("Arial", 12))
res_lbl.pack()

root.mainloop()
