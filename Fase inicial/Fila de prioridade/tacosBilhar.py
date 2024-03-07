nPedidos = int(input())
comprimentoTaco = list(map(int, input().split()))
inicio = time.time()
ListaEstoque = []

for taco in comprimentoTaco:
    if taco not in ListaEstoque:
        ListaEstoque.append(taco)

print(len(ListaEstoque)  * 2)




