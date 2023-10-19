# Данная часть кода служит для
# создания окна и вызова методов
# из другой части  кода для размещения объектов

from tkinter import *  # импорт библиотеки tkinter
from tkinter import ttk

import Raschet  # импорт
import Figure


def MainForm(window):
    window.title("Ипотечный калькулятор для физических лиц")  # установка названия в окне
    window.iconbitmap()  # установка иконки (добавить позже)
    window.geometry("500x600+400+200")  # размер окна (ширина x высота)
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", finish)  # первое - имя события, второе - вызов функции
    window.mainloop()


def finish():
    Frame.destroy()
    print("Закрытие приложения")


Frame = Tk()  # создание графического окна

summa = IntVar()
srok = IntVar()
stavka = DoubleVar()
EveryMonth = IntVar()
Procent = IntVar()
Dolg = IntVar()

r_var = IntVar()
r_var.set(0)


def Vibor():
    if r_var.get() == 0:
        a1 = Raschet.Annuit()
        a1.Raschet(summa, srok, stavka, Procent, EveryMonth, Dolg)
    elif r_var.get() == 1:
        a2 = Raschet.Difference()
        a2.Raschet(summa, srok, stavka, Procent, EveryMonth, Dolg)


btn = ttk.Button(text="Рассчитать", command=Vibor)
btn.place(x=50, y=400)

Label = Figure.Label()
Label.Sozdanie(Frame)
Entry = Figure.Entry(summa, srok, stavka, EveryMonth, Procent, Dolg)
Entry.Sozdanie(Frame)
RadioButton = Figure.RadioButton(r_var)
RadioButton.Sozdanie(Frame)
MainForm(Frame)
