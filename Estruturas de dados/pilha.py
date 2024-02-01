#Lifo (último entrar primeiro a sair)
from queue import LifoQueue
q = LifoQueue()
q.put(1)
q.put(2)
print(q.qsize())
print(q.get())
print(q.get())
print(q.get())