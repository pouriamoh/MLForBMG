



percent = list()
i = 0
while i < 7 :
    va1 = input("input a percent : ")
    if va1 != "Done" :
        percent.append(float(va1))
        i = i+1
    else:
        break

print(percent)

mass = list()
j = 0
while j < 7 :
    va2 = input("input an atomic mass : ")
    if va2 != "Done" :
        mass.append(float(va2))
        j = j+1
    else:
        break

print(mass)




density = list()
j = 0
while j < 7 :
    va2 = input("input a density : ")
    if va2 != "Done" :
        density.append(float(va2))
        j = j+1
    else:
        break

print(density)





vazn = []
for i in range(0, len(percent)):
    vazn.append(percent[i] * mass[i])



totw = sum(vazn)


eachvazn = list()
for item in vazn:
    eachvazn.append(100 * item/totw)

jam = []
for i in range(0, len(percent)):
    jam.append( eachvazn[i] / density[i])


payan = 100/sum(jam)

#import math
#payan = math.sqrt(sum(resu))

print(payan)
