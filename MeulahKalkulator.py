import tkinter
from tkinter import *

root = Tk()
root.title("Simply Kalkulator")
root.geometry("570x600+500+110")
root.resizable(0,0)
root.configure(bg = "#120f41")

equation = ""

def clear():
    global equation
    equation = ""
    label_hasil.config(text=equation)

def show(value):
    global equation
    equation+=value
    label_hasil.config(text=equation)

def menghitung():
    global equation
    result = ""
    if equation != "":
        try:
            result  = eval(equation)
        except:
            result =  "error"
            equation = ""
    label_hasil.config(text=result)


label_hasil = Label(root, width=25, height=2, text="", font=("arial", 30), bg="#7d74ff")
label_hasil.pack()

Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : clear()).place(x= 10, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show("/")).place(x= 150, y=100)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show("%")).place(x= 290, y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show("*")).place(x= 430, y=100)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show("7")).place(x= 10, y=200)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show("8")).place(x= 150, y=200)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show("9")).place(x= 290, y=200)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show("+")).place(x= 430, y=200)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show("4")).place(x= 10, y=300)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show("5")).place(x= 150, y=300)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show("6")).place(x= 290, y=300)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show("-")).place(x= 430, y=300)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show("1")).place(x= 10, y=400)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show("2")).place(x= 150, y=400)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show("3")).place(x= 290, y=400)

Button(root, text="0", width=11, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show("0")).place(x= 10, y=500)
Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : show(".")).place(x= 290, y=500)
Button(root, text="=", width=5, height=int(3.5), font=("arial", 30, "bold"), bd=1, fg= "#fff" ,bg = "#35308a", command=lambda : menghitung()).place(x= 430, y=400)


root.mainloop()