a = "4213"
lista, l = [], []
for c in a:
    lista.append(c)
    l.append(c)
lista.sort()
print(lista)
for i in lista:
    l.remove(i)
    if len(l) + 2 == len(lista):
        break
print(l)
