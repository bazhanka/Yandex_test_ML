# 3
# Moscow 2
# XXXXXXXX.X.X.X.X.X.XXXXX Kvartal
# XXXXXXXXX.X.X.X.X.X.XXXX Kvartet
# Minsk 1
# XX.XXXXX........XXXXXXXX Toloka
# Berlin 2
# XX..XXXXXXXXXXXXXXXXXXXX Mitte
# XXXXXXXXXXXXXXXX.....XXX Lustgarten
# 4
# 3 Moscow Minsk Berlin
# 2 Moscow Minsk
# 2 Minsk Berlin
# 2 Moscow

#15/09/1937

cities = int(input())
d_cities = {}
d_auds = {}
for _ in range(cities):
    city, aud = input().split(" ")
    d_cities[city] = {}
    for el in range (int(aud)):
        time, name = input().split(" ")
        d_cities[city][name] = []
        ind = 0
        while ind < 24:
            if time[ind] == '.':
                d_cities[city][name].append(ind)
                ind += 1
            else:
                ind += 1
meets = int(input())
def get_value(d, key):
    for k, v in d.items():
        if k == key:
            return v
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
def compare(d1,d2):
    ss = {}
    for lk, lv in d1.items():
        for wk, wv in d2.items():
            s = list(set(lv)&set(wv))
            if s:
                ss[f'{lk},{wk}'] = s
            else:
                pass
    return ss

for t in range(meets):
    line = input().split(' ')
    num_cities = int(line[0])
    line.pop(0)
    vs = []
    for el in line:
        v = get_value(d_cities, el)
        vs.append(v)
    index = 0
    ss = compare(vs[index], vs[index + 1])
    while index < len(vs):
        if ss:
            index+=2
            if index>=len(vs):
                print('Yes', list(ss.keys())[-1])
            else:
                ss = compare(ss, vs[index])
        else:
            print('No')
            break