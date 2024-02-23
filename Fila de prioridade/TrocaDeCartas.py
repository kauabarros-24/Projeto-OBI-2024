cartaFulano, cartaCiclano = map(int,input().split())
o = min(cartaCiclano, cartaFulano)

a = list(input().split())
b = list(input().split())

l = []
contador = 0
for _ in range(o):
    if a[0] not in l and b[0] not in l and a[0] != b[0]:
        l.append(a)
        l.append(b)
        contador+=1
    a.remove(a[0])
    b.remove(b[0])

print(contador)






