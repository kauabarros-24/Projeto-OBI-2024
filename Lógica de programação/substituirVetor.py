lista = []
#Ler 10 inteiros
for _ in range(10):
    lista.append(int(input()))

#Imprimir o menor valor:
lista.sort()
print(f"Menor: {lista[0]}")

#Contar quantas vezes aparece o menor valor
print(f"Ocorrencias: {lista.count(lista[0])}")

#Substituir o menor valor por -1:
for i in range(lista.count(lista[0])):
    lista[i] = -1

#Printar
for valor in lista:
    print(valor, end=' ')

