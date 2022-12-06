from tkinter import *
import datetime
root = Tk()
def clear_button():
    day_entrybox.delete(0,END)
    month_entrybox.delete(0,END)
    year_entrybox.delete(0, END)
    given_day_entrybox.delete(0, END)
    given_month_entrybox.delete(0, END)
    given_year_entrybox.delete(0, END)
    years_entrybox.delete(0, END)
    months_entrybox.delete(0, END)
    days_entrybox.delete(0, END)

def calculate_age():
    d1 = int(day_entrybox.get())
    m1 = int(month_entrybox.get())
    y1 = int(year_entrybox.get())
    d2 = int(given_day_entrybox.get())
    m2 = int(given_month_entrybox.get())
    y2 = int(given_year_entrybox.get())

    months1 = [31,28,31,30,31,30,31,31,30,31,30,31]
    if d1>d2:
        m2-=1
        d2+=months1[m1-1]

    if m1>m2:
        y2-=1
        m2+=12

    finalday= d2-d1
    finalmonth = m2-m1
    finalyear = y2-y1

    years_entrybox.insert(0,finalyear)
    months_entrybox.insert(0, finalmonth)
    days_entrybox.insert(0, finalday)







root.title("Age Caclculator")
root.geometry('500x300')
root["bg"]="light blue"
date_of_birth = Label(root,text = "Date of Birth",bg = "red")
date_of_birth.grid(row=0,column=1)

day_entrybox = Entry(root)
day_entrybox.grid(row= 1 , column = 1)

month_entrybox = Entry(root)
month_entrybox.grid(row= 2 , column = 1)


year_entrybox = Entry(root)
year_entrybox.grid(row= 3 , column = 1)

day = Label(root,text = "Day",bg = "light blue")
day.grid(row=1,column=0)

Month = Label(root,text = "Month",bg = "light blue")
Month.grid(row=2,column=0)

year = Label(root,text = "year",bg = "light blue")
year.grid(row=3,column=0)

resultant_age = Button(root, text= "Resultant Age", bg= "black", fg = "white",command = calculate_age)
resultant_age.grid(row = 4, column = 2)

years = Label(root, text = "Years", bg = "light blue")
years.grid(row = 5, column = 2)

years_entrybox = Entry(root)
years_entrybox.grid(row = 6, column = 2)

months = Label(root, text = "Months", bg = "light blue")
months.grid(row = 7, column = 2)

months_entrybox = Entry(root)
months_entrybox.grid(row = 8, column = 2)

days = Label(root, text = "Days", bg = "light blue")
days.grid(row = 9, column = 2)

days_entrybox = Entry(root)
days_entrybox.grid(row = 10, column = 2)

clearall = Button(root, text = "Clear All", bg= "black", fg = "white", command = clear_button)
clearall.grid(row = 11, column = 2)

given_date = Label(root,text = "Given Date",bg = "red")
given_date.grid(row=0,column=4)

given_day_entrybox = Entry(root)
given_day_entrybox.grid(row= 1 , column = 4)

given_month_entrybox = Entry(root)
given_month_entrybox.grid(row= 2 , column = 4)


given_year_entrybox = Entry(root)
given_year_entrybox.grid(row= 3 , column = 4)

given_day = Label(root,text = "Given Day",bg = "light blue")
given_day.grid(row=1,column=3)

given_month = Label(root,text = "Given Month",bg = "light blue")
given_month.grid(row=2,column=3)

given_year = Label(root,text = "Given Year",bg = "light blue")
given_year.grid(row=3,column=3)

root.mainloop()






