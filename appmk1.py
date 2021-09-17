from tkinter import * 

import os

def desligar():
    return os.system("shutdown /s /t 1")
def reiniciar():
    return os.system("shutdown /r /t 1")
def sair():
    return os.system("shutdown -1")

master = Tk()
master.geometry("120x130")

master.configure(bg='light grey')

Button(master, text="Desligar", command=desligar).place(x=100, y=100)
Button(master, text="Reiniciar", command=reiniciar).place(x=100, y=100)
Button(master, text="Sair", command=sair).place(x=100, y=100)

mainloop()