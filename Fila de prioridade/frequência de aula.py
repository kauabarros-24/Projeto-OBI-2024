from queue import PriorityQueue
nPresenca = int(input())

lista = []
pq = PriorityQueue()
for _ in range(nPresenca):
    pq.put(int(input()))
    
contador = 0
l = pq.get()
while pq.qsize() > 0:
    o = pq.get()
    if o == l:
        contador+=1
    l = o

print(nPresenca - contador)

    
    

    