
percent = list()
i = 0
while i < 7 :
    chiz = input("input a percent : ")
    if chiz != "Done" :
        percent.append(float(chiz))
        i = i+1
    else:
        break

print(percent)

radius = list()
j = 0
while j < 7 :
    miz = input("input an radius: ")
    if miz != "Done" :
        radius.append(float(miz))
        j = j+1
    else:
        break

print(radius)


res_list = []
for i in range(0, len(percent)):
    res_list.append(percent[i] * radius[i])



rav = sum(res_list)


atomic = list()
for item in radius:
    atomic.append((1-item/rav)**2)

resu = []
for i in range(0, len(percent)):
    resu.append(percent[i] * atomic[i])


import math
payan = math.sqrt(sum(resu))

print(payan)
