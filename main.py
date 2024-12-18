print('''Введите ваше математическое выражение:''')
a = input().split() + ["###"]
b = ""

def detect(s):
    global cnt
    if s == "один" or s == "одна":
        cnt += 1
        return True
    elif s == "два" or s == "две":
        cnt += 2
        return True
    elif s == "три":
        cnt += 3
        return True
    elif s == "четыре":
        cnt += 4
        return True
    elif s == "пять":
        cnt += 5
        return True
    elif s == "шесть":
        cnt += 6
        return True
    elif s == "семь":
        cnt += 7
        return True
    elif s == "восемь":
        cnt += 8
        return True
    elif s == "девять":
        cnt += 9
        return True
    elif s == "десять":
        cnt += 10
        return True
    elif s == "одиннадцать":
        cnt += 11
        return True
    elif s == "двенадцать":
        cnt += 12
        return True
    elif s == "тринадцать":
        cnt += 13
        return True
    elif s == "четырнадцать":
        cnt += 14
        return True
    elif s == "пятнадцать":
        cnt += 15
        return True
    elif s == "шестнадцать":
        cnt += 16
        return True
    elif s == "семнадцать":
        cnt += 17
        return True
    elif s == "восемнадцать":
        cnt += 18
        return True
    elif s == "девятнадцать":
        cnt += 19
        return True
    elif s == "двадцать":
        cnt += 20
        return True
    elif s == "тридцать":
        cnt += 30
        return True
    elif s == "сорок":
        cnt += 40
        return True
    elif s == "пятьдесят":
        cnt += 50
        return True
    elif s == "шестьдесят":
        cnt += 60
        return True
    elif s == "семьдесят":
        cnt += 70
        return True
    elif s == "восемьдесят":
        cnt += 80
        return True
    elif s == "девяносто":
        cnt += 90
        return True
    elif s == "сто":
        cnt += 100
        return True
    elif s == "двести":
        cnt += 200
        return True
    elif s == "триста":
        cnt += 300
        return True
    elif s == "четыреста":
        cnt += 400
        return True
    elif s == "пятьсот":
        cnt += 500
        return True
    elif s == "шестьсот":
        cnt += 600
        return True
    elif s == "семьсот":
        cnt += 700
        return True
    elif s == "восемьсот":
        cnt += 800
        return True
    elif s == "девятьсот":
        cnt += 900
        return True
    return False

cnt = 0
res = 0

for j in range(0, len(a)):
    i = a[j]
    if i == '(':
        b += i
    elif i == ')':
        res += cnt
        cnt = 0
        if res:
            b += str(res)
            res = 0
        b += i
    elif i == "плюс":
        res += cnt
        cnt = 0
        if res:
            b += str(res)
            res = 0
        b += '+'
    elif i == "минус":
        res += cnt
        cnt = 0
        if res:
            b += str(res)
            res = 0
        b += '-'
    elif i == "умножить":
        res += cnt
        cnt = 0
        if res:
            b += str(res)
            res = 0
        b += '*'
    elif i == "делить":
        res += cnt
        cnt = 0
        if res:
            b += str(res)
            res = 0
        b += '/'
    elif i == "степени":
        res += cnt
        cnt = 0
        if res:
            b += str(res)
            res = 0
        b += "**"
    elif i == "остатке":
        res += cnt
        cnt = 0
        if res:
            b += str(res)
            res = 0
        b += '%'
    else:
        if detect(i):
            pass
        elif i.find("тыс") != -1:
            cnt *= 1000
            res += cnt
            cnt = 0
        elif i.find("миллион") != -1:
            cnt *= 1000000
            res += cnt
            cnt = 0
        elif i.find("миллиард") != -1:
            cnt *= 1000000000
            res += cnt
            cnt = 0
        elif cnt:
            res += cnt
            cnt = 0
        elif res:
            res += cnt
            cnt = 0
            b += str(res)
            res = 0
    #print("res: " + str(res) + "; cnt: " + str(cnt) + "; b: " + b)

res += cnt
cnt = 0
if res:
    b += str(res)
    res = 0

print(eval(b))