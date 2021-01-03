from tkinter import *

window = Tk()
window.title("Miles / KM Converter")
window.config(padx=100,pady=100)

window.minsize(width=500, height=500)

def calculate():
    miles = float(entry.get())
    result_label.config(text=round(miles*1.609,2))

entry = Entry(width=5)
entry.grid(column=1,row=0)
entry.focus()

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0,row=1)

result_label = Label(text=0)
result_label.grid(column=1,row=1)
result_label.config(padx=20,pady=20)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1,row=3)

window.mainloop()