from tkinter import *

#OPTION : X,Y,HEIGHT,WIDTH, RELX, RELY, RELHEIGHT, RELWIDTH, ANCHOR, BORDERMODE
#ANCHOR : N(ATAS), W(KIRI), S(BAWAH), E(KANAN), BISA DIGABUNG
#BORDERMODE : INDSIDE, OUTSIDE
window = Tk()
window.geometry("500x500+500+170")
Button1 = Button(text="Tombol1")
Button1.place(relwidth=0.3, relheight=0.3, bordermode="outside")

window.mainloop()