from abc import ABC, abstractmethod


class Method(ABC):

    def Annuit(self):
        pass

    def Annuit(self, summa, srok, stavka, procent, everyMonth, dolg):
        srok = srok.get() * 12
        everyMonthStavka = stavka.get() / (12 * 100)
        globalStavka = (1 + everyMonthStavka) ** srok
        everyMonth1 = int((summa.get() * everyMonthStavka * globalStavka) / (globalStavka - 1))
        procent1 = int(everyMonth1 * srok - summa.get())
        dolg1 = int(procent1 + summa.get())
        procent.set(procent1)
        everyMonth.set(everyMonth1)
        dolg.set(dolg1)

    def Differenc(summa, srok, stavka, procent, everyMonth, dolg):  # данные, которые будут получены из полей ввода
        global procentPart, accuredInterest, ostatok, dolg1, monthlyPayment  # данные для расчетов внутри функции
        accuredInterest = 0
        srok = srok.get() * 12  # получаем содержимое поля ввода
        everyMonthStavka = stavka.get() / (12 * 100)  # ежемесячная ставка
        everyMonthDolg = summa.get() / srok  # ежемесячнео погашение долга
        ostatok = summa.get()  # начальный остаток по платежу
        MaxEveryMonth = ostatok * everyMonthStavka + everyMonthDolg  # маскимальный платеж в первый месяц
        for i in range(1, srok + 1, 1):  # цикл до последнего месяца платежа
            procentPart = ostatok * everyMonthStavka
            monthlyPayment = procentPart + everyMonthDolg
            ostatok -= everyMonthDolg
            accuredInterest += procentPart
        dolg1 = summa.get() + accuredInterest
        MinEveryMonth = everyMonthDolg
        procent.set(accuredInterest)
        everyMonth.set(MinEveryMonth)
        dolg.set(dolg1)
