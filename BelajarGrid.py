from tkinter import *

#Option :  Sticky, column, row, columnspan, rowspan, padx, pady, ipadx, ipady
#Sticky : Atas(n), Bawas(s), Kanan(w), Kiri(e)
Window = Tk()
Window.geometry("500x500+480+180")

Window.columnconfigure(0, weight=1)
Window.columnconfigure(1, weight=1)
Window.columnconfigure(2, weight=1)
Window.columnconfigure(3, weight=1)

#Ini kolom ke sb y

Window.rowconfigure(0, weight=1)
Window.rowconfigure(1, weight=1)
#ini kolom per shaf atau per sb x
Tombol1 = Button(text="Tombol1")
Tombol2 = Button(text="Tombol2")
Tombol3 = Button(text="Tombol3")
Tombol4 = Button(text="Tombol4")

Tombol1.grid(column= 0, row=0, sticky="we",)
Tombol2.grid(column= 0, row=1, sticky="we",)
Tombol3.grid(column= 1, row=0, sticky="we",)
Tombol4.grid(column= 1, row=1, sticky="we",)

Window.mainloop()