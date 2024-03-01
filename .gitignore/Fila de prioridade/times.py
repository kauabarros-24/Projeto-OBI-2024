from queue import PriorityQueue

quantidadeJogadores, nTimes = map(int, input().split())
lista = []
for _ in range(quantidadeJogadores):
    subLista = []
    nomejogador, skillJogador = map(str, input().split())
    subLista.append(skillJogador)
    subLista.append(nomejogador)
    lista.append(subLista)


listaOrdenada = sorted(lista, key=lambda x: int(x[0]), reverse=True)

i = 0
while i < nTimes:
    pq = PriorityQueue()
    for c, t in listaOrdenada[i::nTimes]: 
        pq.put(t)
    print(f"Time {i + 1}")
    while pq.qsize() > 0:
        print(pq.get())  
    print("")
    i += 1
