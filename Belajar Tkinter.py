import tkinter as Tk
from tkinter import *
#ini cara meimport tkinter

window = Tk()
#jadi kita meulah variabel yang makai function tkinter

#meulah variabel gsn meatur window muncul dari tkinter
Lebar = 500
Tinggi = 500
screenwidht = window.winfo_screenwidth()
#ini jadi kita bisi variabel namnya screenwidth yang meambil dari lebar dari layar laptop
screenhigh = window.winfo_screenheight()

x = int((screenwidht/2) - (Lebar/2))
y = int((screenhigh/2) - (Tinggi/2)) - 98
#ini variabel gsn meatur letak pas window nya tebuka

window.geometry(f"{Lebar}x{Tinggi}+{x}+{y}")
#ini cara makai variable di atas
window.resizable(0,0)
#ini meulah window nya kd kw di resize
window.title("Belajar Tkinter Dari Awal")
#inin cara meubah judul
window.mainloop()