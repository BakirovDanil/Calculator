from tkinter import*
from tkinter import ttk

clicks = 0
def finish():
    window.destroy()
    print("Закрытие приложения")
def click():
    global clicks
    clicks +=1
    btn["text"]=f"Клик {clicks}"
    if clicks>=5:
        btn["state"]="disabled"

window=Tk() #создание графического окна
window.title("Ипотечный калькулятор для физических лиц") #установка названия в окне
window.iconbitmap() #установка иконки (добавить позже)
window.geometry("500x600+400+200") #размер окна (ширина x высота)
window.resizable(False,False)
window.protocol("WM_DELETE_WINDOW", finish) #первое - имя события, второе - вызов функции

def sozdanieLabel(Tk):
    summa = ttk.Label(text="Сумма кредита:")
    summa.place(x=25, y=25)  # размещение метки в окне

    srok = ttk.Label(text="Срок кредита:")
    srok.place(x=25, y=60)  # размещение метки в окне

    stavka = ttk.Label(text="Ключевая ставка:")
    stavka.place(x=25, y=95)  # размещение метки в окне

    type = ttk.Label(text="Выбрать тип расчета:")
    type.place(x=25, y=130)  # размещение метки в окне
def sozdanieEntry(Tk):
    entr1=ttk.Entry(width=10)
    entr1.place(x=185, y=25)

    entr1 = ttk.Entry(width=10)
    entr1.place(x=185, y=60)

    entr1 = ttk.Entry(width=10)
    entr1.place(x=185, y=95)

    entr1 = ttk.Entry(width=10)
    entr1.place(x=185, y=130)

btn=ttk.Button(text="Нажми")
btn["command"]=click
btn.place()

sozdanieLabel(window)
sozdanieEntry(window)
window.mainloop() #цикл обработки событий окна при взаимодействии пользователя