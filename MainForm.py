from tkinter import *
from tkinter import ttk

import Raschet


def finish():
    window.destroy()
    print("Закрытие приложения")


window = Tk()  # создание графического окна

summa = IntVar()
srok = IntVar()
stavka = DoubleVar()
EveryMonth = IntVar()
Procent = IntVar()
Dolg = IntVar()


def MainForma(Tk):
    window.title("Ипотечный калькулятор для физических лиц")  # установка названия в окне
    window.iconbitmap()  # установка иконки (добавить позже)
    window.geometry("500x600+400+200")  # размер окна (ширина x высота)
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", finish)  # первое - имя события, второе - вызов функции


r_var = IntVar()
r_var.set(0)


def Vibor():
    if r_var.get() == 0:
        a1 = Raschet.Annuit()
        a1.Raschet(summa, srok, stavka, Procent, EveryMonth, Dolg)
    elif r_var.get() == 1:
        a2 = Raschet.Difference()
        a2.Raschet(summa, srok, stavka, Procent, EveryMonth, Dolg)


class Sozdanie():
    summaLabel = ttk.Label(text="Сумма кредита:")
    srokLabel = ttk.Label(text="Срок кредита:")
    stavkaLabel = ttk.Label(text="Ключевая ставка:")
    typeLabel = ttk.Label(text="Тип ежемесячных платежей:")
    EveryMonthLabel = ttk.Label(text="Ежемесячный платеж")
    ProcentLabel = ttk.Label(text="Начисленные проценты")
    DolgLabel = ttk.Label(text="Сумма долга")

    def sozdanieLabel(Tk):
        Sozdanie.summaLabel.place(x=25, y=25)  # размещение метки в окне (Сумма кредита)
        Sozdanie.srokLabel.place(x=25, y=60)  # размещение метки в окне (Срок кредита)
        Sozdanie.stavkaLabel.place(x=25, y=95)  # размещение метки в окне (Ключевая ставка)
        Sozdanie.typeLabel.place(x=25, y=150)  # размещение метки в окне (Тип ежемесячных платежей)
        Sozdanie.EveryMonthLabel.place(x=25, y=260)  # размещение метки в окне (Ежемесячгый платеж)
        Sozdanie.ProcentLabel.place(x=25, y=295)  # размещение метки в окне (Начисленные проценты)
        Sozdanie.DolgLabel.place(x=25, y=330)  # размещение метки в окне (Сумма долга)

    entr1 = ttk.Entry(width=10, textvariable=summa)
    entr2 = ttk.Entry(width=10, textvariable=srok)
    entr3 = ttk.Entry(width=10, textvariable=stavka)
    entr4 = ttk.Entry(width=10, textvariable=EveryMonth)
    entr5 = ttk.Entry(width=10, textvariable=Procent)
    entr6 = ttk.Entry(width=10, textvariable=Dolg)

    def sozdanieEntry(Tk):
        Sozdanie.entr1.place(x=185, y=25)
        Sozdanie.entr2.place(x=185, y=60)
        Sozdanie.entr3.place(x=185, y=95)
        Sozdanie.entr4.place(x=200, y=260)
        Sozdanie.entr5.place(x=200, y=295)
        Sozdanie.entr6.place(x=200, y=330)

    annuit = ttk.Radiobutton(text="Аннуитетные платежи", variable=r_var, value=0)
    differenc = ttk.Radiobutton(text="Дифференцированные платежи", variable=r_var, value=1)

    def SozdanieRadioButton(Tk, r_var):
        Sozdanie.annuit.place(x=25, y=200)
        Sozdanie.differenc.place(x=25, y=235)


btn = ttk.Button(text="Рассчитать", command=Vibor)
btn.place(x=50, y=400)
MainForma(window)
Sozdanie.sozdanieLabel(window)
Sozdanie.sozdanieEntry(window)
Sozdanie.SozdanieRadioButton(window, r_var)
window.mainloop()
