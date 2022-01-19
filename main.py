import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

janela = Tk()
janela.title("Auto Reload - Lojas Edmil")
janela.iconbitmap('image.ico')
janela.resizable(False,False)

var = StringVar()
var1 = IntVar()
var2 = IntVar()
var4 = StringVar()

def pegar_nome():
    content = var.get()
    hora = var1.get()
    horafinal = var2.get()
    caminhofinal = var4.get()
    print(horainicial)
    print(horafinal)
    print(content)

    # COMANDO CMD#
    os.system(f'taskkill /f /im {content}')
    # FINAL COMANDO CMD#

nome = Label(janela, text= "Insira os dados abaixo:", font="6")
nome.grid(padx=10,pady=10,columnspan=4,row=0)

solicitacaminho = Label(janela, text= "Email:")
solicitacaminho.grid(column=0,row=2,padx=5,pady=5)

caminho = Entry(janela, textvariable=var4, width=30)
caminho.grid(column=1,row=2,padx=5,pady=5,columnspan=2, sticky=W)
#caminho.set(r'C:\sisedmil\autointbenner\splash.exe "AutoIntBenner" autointbenner.exe')
caminho.get()


horarios = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
hr = ttk.Combobox(janela, values=horarios, textvariable=var1, width=5)
hr.set("21")
hr.grid(column=1, row=3, padx=5, pady=5, sticky=W)
hr.get()

bt = Button (janela, width=20, text="Iniciar/Parar", command=pegar_nome)
bt.grid(columnspan=4,row=4,padx=20,pady=20)

janela.mainloop()