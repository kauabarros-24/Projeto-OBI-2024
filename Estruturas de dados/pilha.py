from queue import LifoQueue
a = "{[]}"
#print(a[0])
#b = a.replace(a[0], "").replace(a[1], "")
#a = b
#print(b)
#print(a)
t = 0
for x in a:
    if x == a[-1]:
       break
    subA = a.replace(a[t], "")
    print(subA)
    i = 1
    print(x, "mestre")
    for y in subA:
        print(y)
    i+=1
    t+=1


        
    