from queue import LifoQueue
q = LifoQueue()
#q.put("Olá")
#a = q.get()
#print(a)
#print(q.qsize())
#q.put(a)
#print(q.qsize())
#c = "Ola"
#print(c[0])
c = "OlO"
#for i in enumerate(c[1:], 1):
    #print(i)
#c.remove(c[0])
#a = c - c[0]
#c = a
print(q.qsize())#print(a)
q.put(1)
if q.get() == 1:
    print("Sim")

