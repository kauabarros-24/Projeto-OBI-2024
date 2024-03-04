lista = []
listaOcorrer = []
#Ler 10 inteiros
for _ in range(10):
    lista.append(int(input()))

#Imprimir o menor valor:
lista.sort()
print(f"Menor: {lista[0]}")

#Armzenar as posições na qual aparece o menor valor:
contador = 0
for c in lista:
    if c == lista[0]:
        listaaOcorrer




#Substituir o menor valor por -1:
for i in range(lista.count(lista[0])):
    lista[i] = -1

#Printar
for valor in lista:
    print(valor, end=' ')

