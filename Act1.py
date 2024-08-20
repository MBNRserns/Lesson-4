from tkinter import *
import calendar
root = Tk()
root.config(background="White")
root.title("Calendar")
root.geometry("250x140")

def showCal():
    gui = Tk()
    gui.config(background="White")
    gui.title("Calendar")
    gui.geometry("550x600")
    fetch_year = int(year_field.get())
    print("fetch_year",fetch_year)
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(gui,text=cal_content, font="Consolas 10 bold")
    cal_year.grid(row=5, column=1, padx=20)
    gui.mainloop()


cal = Label(root,text="CALENDAR", bg="dark gray", font=("times", 28, "bold"))
cal.grid(row=1, column=1)

year = Label(root,text="Enter Year", bg="gray")
year.grid(row=2, column=1)

year_field = Entry(root)
year_field.grid(row=3, column=1)

show = Button(root, text="Show Calendar", fg="Black",bg="Red", command=showCal)
show.grid(row=4, column=1)

exit = Button(root, text="Exit", fg="Black",bg="Red", command=exit)
exit.grid(row=5, column=1)

root.mainloop()