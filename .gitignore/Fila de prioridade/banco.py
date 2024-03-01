lista = []

quantidadeCaixas, numeroClientes = map(int, input().split())
if quantidadeCaixas >= numeroClientes:
    print(0)

for c in range(numeroClientes):
    chegada, tempoAtendimento = map(int, input().split())
    lista.append(tempoAtendimento)

lista.sort()
print(lista)


    


