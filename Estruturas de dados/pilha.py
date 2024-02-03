a = "()}]"
#print(a[0])
#b = a.replace(a[0], "").replace(a[1], "")
#a = b
#print(b)
#print(a)

for x in a:
    if x == a[-1]:
        break
    i = 1
    print(x, "mestre")
    for y in enumerate(a[i:], 2):
        print(y)
    l = a.replace(x, a[i])
    a = l
    a.s
    i+=1
    