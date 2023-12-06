
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

vec = list()
j = 0
while j < 7 :
    miz = input("input a vec : ")
    if miz != "Done" :
        vec.append(float(miz))
        j = j+1
    else:
        break

print(vec)


res_list = []
for i in range(0, len(percent)):
    res_list.append(percent[i] * vec[i])



jam = sum(res_list)

'''

atomic = list()
for item in paul:
    atomic.append((item - pav)**2)

resu = []
for i in range(0, len(percent)):
    resu.append(percent[i] * atomic[i])


import math
payan = math.sqrt(sum(resu))




'''

print(jam)
