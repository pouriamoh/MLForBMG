
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

vec = list()
j = 0
while j < 7 :
    va2 = input("input a vec : ")
    if va2 != "Done" :
        vec.append(float(va2))
        j = j+1
    else:
        break

print(vec)


res_list = []
for i in range(0, len(percent)):
    res_list.append(percent[i] * vec[i])



jam = sum(res_list)


print(jam)
