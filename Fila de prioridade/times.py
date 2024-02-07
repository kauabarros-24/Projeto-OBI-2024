from queue import PriorityQueue
import time

quantidadeJogadores, nTimes = map(int, input().split())
inicio = time.time()
lista = []
for _ in range(quantidadeJogadores):
    subLista = []
    nomejogador, skillJogador = map(str, input().split())
    subLista.append(skillJogador)
    subLista.append(nomejogador)
    lista.append(subLista)
    
lista.sort(reverse=True)

i, k = 0, 0
while i < nTimes:
    pq = PriorityQueue()
    for c, t in enumerate(lista[i: (quantidadeJogadores - nTimes) + k]): 
        print(c, t)
        pq.put(t)
        k+=1
    print(f"Time {i + 1}")
    while pq.qsize() > 0:
        print(pq.get())  
    print("")
    i += 1
fim = time.time()
print(fim - inicio)
