values = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 40:"XL", 50:"L", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I", 0:None}
x = input("Number to be converted: ")
z = []

def single():
    f = x[-1]
    f = int(f)
    if f == 0:
        pass
    elif f <= 3:
        z.append(values[1] * f)
    elif f == 4:
        z.append(values[4])
    elif 4 < f <= 8:
        z.append(values[5] + (values[1] * (f - 5)))
    elif f == 9:
        z.append(values[9])
    return

def tens():
    t = x[-2]
    t = int(t)
    if t == 0:
        pass
    elif t <= 3:
        z.append(values[10] * t)
    elif t == 4:
        z.append(values[40])
    elif 4 < t <=8 :
        z.append(values[50] + (values[10] * (t - 5)))
    elif t == 9:
        z.append(values[90])
    return


def hundereds():
    h = x[-3]
    h = int(h)
    if h == 0:
        pass
    elif h <= 3:
        z.append(values[100] * h)
    elif h == 4:
        z.append(values[400])
    elif 4 < h <=8 :
        z.append(values[500] + (values[100] * (h - 5)))
    elif h == 9:
        z.append(values[900])
    return

def thousands():
    th = x[-4]
    th = int(th)
    if th == 0:
        pass
    elif th <= 3:
        z.append(values[1000] * th)
    return

if len(x) == 2:
    single()
    tens()
elif len(x) == 3:
    single()
    tens()
    hundereds()
elif len(x) == 4:
    single()
    tens()
    hundereds()
    thousands()


z.reverse()
g = ''.join(z)
print(g)