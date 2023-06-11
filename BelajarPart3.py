from tkinter import *

#Belajar Layout Management

window = Tk()

window.geometry("550x500+470+180")

Tombol1 = Button(text="Jangan Dipencet")
Tombol1.pack(expand=YES, fill=NONE, padx=50, pady=50, ipadx=10, ipady=10)
Tombol2 = Button(text="Dipencet")
Tombol2.pack(expand=YES, fill=NONE, padx=50, pady=50, ipadx=10, ipady=10)
Tombol3 = Button(text="Boleh Dipencet")
Tombol3.pack(expand=YES, fill=NONE, padx=50, pady=50, ipadx=10, ipady=10)
#side : top, bottom, left, right
#fill : none, x, y, both
#expand : yes, no
#padx, pady, ipadx, ipady
window.mainloop()



















