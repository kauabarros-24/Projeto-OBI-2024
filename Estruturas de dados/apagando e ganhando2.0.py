from queue import PriorityQueue, LifoQueue, SimpleQueue
import time
while True:
    inicio = time.time()
    tamanhoN, retirarD = map(int, input().split())
    if tamanhoN == 0 and retirarD == 0:
        break
    a, num, pq = str(input()), [], PriorityQueue()
    for c in a:
        num.append(c)
        pq.put(c)
    for i in range(retirarD):
        num.remove(pq.get())
    resp =  ''.join(map(str, num))
    print(resp)
    fim = time.time()
    print(fim - inicio)
