#ini code yang di part 1

#Belajar EVent dan biding
#ini pas mouse lwn keyboard di pakai

from tkinter import *

window = Tk()

def eventButton(event):
    print(event.num)

window.bind("<Button>", eventButton)
window.mainloop()