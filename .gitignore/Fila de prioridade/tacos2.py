nPedidos = int(input())
listaComprimento = input().split(" ")
set = set()

for c in range(nPedidos):
    consulta = listaComprimento[c]
    if consulta not in set:
        set.add(consulta)

print(len(set) * 2)