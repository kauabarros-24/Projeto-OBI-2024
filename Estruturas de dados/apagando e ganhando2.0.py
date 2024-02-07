from queue import PriorityQueue

while True:
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
