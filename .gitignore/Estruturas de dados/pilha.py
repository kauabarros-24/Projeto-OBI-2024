a = ["324"] 
b = []
i = 0
for c in a:
    b.append(c)
    print(c)
b.sort()
for k in b:
    if i == 2:
        break
    a.remove(k)
    i+=1
print(a)