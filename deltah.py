
first = list()
i = 0
while i < 7 :
    chiz = input("input first percent : ")
    if chiz != "Done" :
        first.append(float(chiz))
        i = i+1
    else:
        break

print(percent)

paul = list()
j = 0
while j < 7 :
    miz = input("input an pauling electro : ")
    if miz != "Done" :
        paul.append(float(miz))
        j = j+1
    else:
        break

print(paul)


res_list = []
for i in range(0, len(percent)):
    res_list.append(percent[i] * paul[i])



pav = sum(res_list)


atomic = list()
for item in paul:
    atomic.append((item - pav)**2)

resu = []
for i in range(0, len(percent)):
    resu.append(percent[i] * atomic[i])


import math
payan = math.sqrt(sum(resu))

print(payan)
