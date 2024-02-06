a = [3, 2, 4]
b = []
b.append(a)
b.sort()
print(b)
print(a)
i = 0
while i <= 1:
    print(b)
    a.remove(b[i])
    print(b)
    i+=1