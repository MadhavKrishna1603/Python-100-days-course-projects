from tkinter import *

def calculate():
    user_input = int(mile.get())
    km = round(user_input*1.609)
    label3.config(text=km,font=("Cursive",15,"italic"))


window = Tk()
window.minsize(height=500,width=500)
window.title("mile to km converter")
window.config(padx=20,pady=20)

mile = Entry()

mile.grid(column=1,row=0)

label1 = Label(text="Miles",font=("Cursive",15,"italic"))
label1.grid(column=2,row=0)

label2 = Label(text="is equal to",font=("Cursive",15,"italic"))
label2.grid(column=0,row=1)

label3 = Label(text=0,font=("Cursive",15,"italic"))
label3.grid(column=1,row=1)
label3.config(padx=3,pady=3)

label4 = Label(text="Km",font=("Cursive",15,"italic"))
label4.grid(column=2,row=1)

button = Button(text="Calculate",width=7,command=calculate)
button.grid(column=1,row=2)


window.mainloop()
