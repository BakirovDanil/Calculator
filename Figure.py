from abc import ABC
from tkinter import ttk


class Figure(ABC):

    def Sozdanie(self, window):
        pass


class Label(Figure):

    def Sozdanie(self, window):
        summaLabel = ttk.Label(text="Сумма кредита:")
        srokLabel = ttk.Label(text="Срок кредита:")
        stavkaLabel = ttk.Label(text="Ключевая ставка:")
        typeLabel = ttk.Label(text="Тип ежемесячных платежей:")
        EveryMonthLabel = ttk.Label(text="Ежемесячный платеж")
        ProcentLabel = ttk.Label(text="Начисленные проценты")
        DolgLabel = ttk.Label(text="Сумма долга")
        summaLabel.place(x=25, y=25)  # размещение метки в окне (Сумма кредита)
        srokLabel.place(x=25, y=60)  # размещение метки в окне (Срок кредита)
        stavkaLabel.place(x=25, y=95)  # размещение метки в окне (Ключевая ставка)
        typeLabel.place(x=25, y=150)  # размещение метки в окне (Тип ежемесячных платежей)
        EveryMonthLabel.place(x=25, y=260)  # размещение метки в окне (Ежемесячгый платеж)
        ProcentLabel.place(x=25, y=295)  # размещение метки в окне (Начисленные проценты)
        DolgLabel.place(x=25, y=330)  # размещение метки в окне (Сумма долга)


class Entry(Figure):
    def __init__(self, summa, srok, stavka, EveryMonth, Procent, Dolg):
        self.summa = summa
        self.srok = srok
        self.stavka = stavka
        self.EveryMonth = EveryMonth
        self.Procent = Procent
        self.Dolg = Dolg

    def Sozdanie(self, window):
        entr1 = ttk.Entry(width=10, textvariable=self.summa)
        entr2 = ttk.Entry(width=10, textvariable=self.srok)
        entr3 = ttk.Entry(width=10, textvariable=self.stavka)
        entr4 = ttk.Entry(width=10, textvariable=self.EveryMonth, state="readonly")
        entr5 = ttk.Entry(width=10, textvariable=self.Procent, state="readonly")
        entr6 = ttk.Entry(width=10, textvariable=self.Dolg, state="readonly")
        entr1.place(x=185, y=25)
        entr2.place(x=185, y=60)
        entr3.place(x=185, y=95)
        entr4.place(x=200, y=260)
        entr5.place(x=200, y=295)
        entr6.place(x=200, y=330)


class RadioButton(Figure):
    def __init__(self, r_var):
        self.r_var = r_var

    def Sozdanie(self, window):
        annuit = ttk.Radiobutton(text="Аннуитетные платежи", variable=self.r_var, value=0)
        differenc = ttk.Radiobutton(text="Дифференцированные платежи", variable=self.r_var, value=1)
        annuit.place(x=25, y=185)
        differenc.place(x=25, y=220)
