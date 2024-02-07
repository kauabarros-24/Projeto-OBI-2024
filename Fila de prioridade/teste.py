from queue import SimpleQueue, LifoQueue, PriorityQueue

sq, pq = SimpleQueue(), PriorityQueue()
sq.put(3)
sq.put(20)
sq.put(1)
pq.put(3)
pq.put(20)
pq.put(1)

print(sq.get(), sq.get(), sq.get())
print(pq.get(), pq.get(), pq.get())
