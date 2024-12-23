print('''Ввод выражения осуществляется словами из русского языка,
записанными, соответствуя орфографическим и грамматическим
нормам. Все слова и скобки должны быть разделены пробелом.
Всего доступно 6 операций:
1. Сложение. Осуществляется написанием "плюс" между слагаемыми.
   Пример: "два плюс четыре".
2. Вычитание. Осуществляется написанием "минус" между частями.
   Пример: "два минус четыре".
3. Умножение. Осуществляется написанием "умножить на" между частями.
   Пример: "два умножить на четыре".
4. Деление. Осуществляется написанием "делить на" между частями.
   Пример: "два делить на четыре".
5. Деление по модулю. Осуществляется написанием "в остатке на" между частями.
   Пример: "два в остатке на четыре".
6. Возведение в степень. Осуществляется написанием "в степени" между частями.
   Пример: "два в степени четыре".

Введите ваше математическое выражение:''')
a = input().split() + ["###"]              #разбиваем строку на слова
b = ""                                     #строка для ответа

def detect(s):                             #функция которая определяет является ли строка частью числа и если да возвращает True
    global cnt, can
    if s == "ноль":                        #если строка равна нулю
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "один" or s == "одна":       #если строка равна одному
        cnt += 1                           #прибавляем 1 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "два" or s == "две":         #если строка равна двум
        cnt += 2                           #прибавляем 2 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "три":                       #если строка равна трём
        cnt += 3                           #прибавляем 3 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "четыре":                    #если строка равна четырём
        cnt += 4                           #прибавляем 4 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "пять":                      #если строка равна пяти
        cnt += 5                           #прибавляем 5 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "шесть":                     #если строка равна шести
        cnt += 6                           #прибавляем 6 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "семь":                      #если строка равна семи
        cnt += 7                           #прибавляем 7 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "восемь":                    #если строка равна восьми
        cnt += 8                           #прибавляем 8 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "девять":                    #если строка равна девяти
        cnt += 9                           #прибавляем 9 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "десять":                    #если строка равна десяти
        cnt += 10                          #прибавляем 10 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "одиннадцать":               #если строка равна одиннадцати
        cnt += 11                          #прибавляем 11 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "двенадцать":                #если строка равна двенадцати
        cnt += 12                          #прибавляем 12 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "тринадцать":                #если строка равна тринадцати
        cnt += 13                          #прибавляем 13 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "четырнадцать":              #если строка равна четырнадцати
        cnt += 14                          #прибавляем 14 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "пятнадцать":                #если строка равна пятнадцати
        cnt += 15                          #прибавляем 15 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "шестнадцать":               #если строка равна шестнадцати
        cnt += 16                          #прибавляем 16 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "семнадцать":                #если строка равна семнадцати
        cnt += 17                          #прибавляем 17 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "восемнадцать":              #если строка равна восемнадцати
        cnt += 18                          #прибавляем 18 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "девятнадцать":              #если строка равна девятнадцати
        cnt += 19                          #прибавляем 19 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "двадцать":                  #если строка равна двадцати
        cnt += 20                          #прибавляем 20 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "тридцать":                  #если строка равна тридцати
        cnt += 30                          #прибавляем 30 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "сорок":                     #если строка равна сорока
        cnt += 40                          #прибавляем 40 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "пятьдесят":                 #если строка равна пятидесяти
        cnt += 50                          #прибавляем 50 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "шестьдесят":                #если строка равна шестидесяти
        cnt += 60                          #прибавляем 60 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "семьдесят":                 #если строка равна семидесяти
        cnt += 70                          #прибавляем 70 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "восемьдесят":               #если строка равна восьмидесяти
        cnt += 80                          #прибавляем 80 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "девяносто":                 #если строка равна девяноста
        cnt += 90                          #прибавляем 90 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "сто":                       #если строка равна стам
        cnt += 100                         #прибавляем 100 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "двести":                    #если строка равна двумстам
        cnt += 200                         #прибавляем 200 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "триста":                    #если строка равна трёмстам
        cnt += 300                         #прибавляем 300 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "четыреста":                 #если строка равна четырёмстам
        cnt += 400                         #прибавляем 400 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "пятьсот":                   #если строка равна пятистам
        cnt += 500                         #прибавляем 500 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "шестьсот":                  #если строка равна шестистам
        cnt += 600                         #прибавляем 600 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "семьсот":                   #если строка равна семистам
        cnt += 700                         #прибавляем 700 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "восемьсот":                 #если строка равна восьмистам
        cnt += 800                         #прибавляем 800 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    elif s == "девятьсот":                 #если строка равна девятистам
        cnt += 900                         #прибавляем 900 к счётчику
        if not can:                        #если до этого было не это же число
            can = True                     #то теперь это это число
        return True                        #возвращаем True
    return False                           #иначе возвращает False

cnt = 0                                    #переменная хранящая в себе 3 цифры какого-то блока
res = 0                                    #переменная хранящая с себе всё число
can = False                                #переменная определяющая обрабатывали ли мы сейчас часть числа

for j in range(0, len(a)):                 #идём по элементам словам из строки
    i = a[j]
    if i == '(':                           #если текущий элемент - '('
        b += i                             #добавляем его в конец строки
    elif i == ')':                         #если текущий элемент - ')'
        res += cnt                         #обновляем всё число
        cnt = 0
        if can:                            #добавляем число к строке
            b += str(res)
            res = 0
        b += i                             #добавляем его в конец строки
        can = False
    elif i == "плюс":                      #если текущий элемент - '+'
        res += cnt
        cnt = 0
        if can:                            #добавляем число к строке
            b += str(res)
            res = 0
        b += '+'                           #добавляем его в конец строки
        can = False
    elif i == "минус":                     #если текущий элемент - '-'
        res += cnt
        cnt = 0
        if can:                            #добавляем число к строке
            b += str(res)
            res = 0
        b += '-'                           #добавляем его в конец строки
        can = False
    elif i == "умножить":                  #если текущий элемент - '*'
        res += cnt
        cnt = 0
        if can:                            #добавляем число к строке
            b += str(res)
            res = 0
        b += '*'                           #добавляем его в конец строки
        can = False
    elif i == "делить":                    #если текущий элемент - '/'
        res += cnt
        cnt = 0
        if can:                            #добавляем число к строке
            b += str(res)
            res = 0
        b += '/'                           #добавляем его в конец строки
        can = False
    elif i == "степени":                   #если текущий элемент - '**'
        res += cnt
        cnt = 0
        if can:                            #добавляем число к строке
            b += str(res)
            res = 0
        b += "**"                          #добавляем его в конец строки
        can = False
    elif i == "остатке":                   #если текущий элемент - '%'
        res += cnt
        cnt = 0
        if can:                            #добавляем число к строке
            b += str(res)
            res = 0
        b += '%'                           #добавляем его в конец строки
        can = False
    else:
        if detect(i):                      #если строка - часть числа
            pass                           #пропускаем
        elif i.find("тыс") != -1:          #если текущая строка - одно из склонений слова "тысяча"
            cnt *= 1000                    #домножаем часть на 1000
            res += cnt                     #добавляем к ответу
            cnt = 0
        elif i.find("миллион") != -1:      #если текущая строка - одно из склонений слова "миллион"
            cnt *= 1000000                 #домножаем часть на 1000000
            res += cnt                     #добавляем к ответу
            cnt = 0
        elif i.find("миллиард") != -1:     #если текущая строка - одно из склонений слова "миллиард"
            cnt *= 1000000000              #домножаем часть на 1000000
            res += cnt                     #добавляем к ответу
            cnt = 0
        elif cnt:                          #если не то и не то и часть не равна нулю
            res += cnt                     #добавляем часть к числу
            cnt = 0
        elif can:                          #если число не равно 0
            res += cnt                     #обновляем число
            cnt = 0
            b += str(res)                  #добавляем число к выражению
            res = 0
    #print("res: " + str(res) + "; cnt: " + str(cnt) + "; b: " + b)

res += cnt
cnt = 0
if can:                                    #если мы можем
    b += str(res)                          #добавляем в конец строки последнее слагаемое
    res = 0

print(eval(b))                             #вычисляем решение выражения
