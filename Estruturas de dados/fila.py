from queue import SimpleQueue

q = SimpleQueue()
print(type(q))

q.put(1)
print(q)
q.put(2)
print(q)
print(q.qsize())
print(q.get())
print(q.qsize())
