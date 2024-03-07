from queue import PriorityQueue

#Criando uma priority queue
pq = PriorityQueue()

#Inserção de elementos
pq.put(3)
pq.put(20)
pq.put(1)


#Remoção do primeito elemento:
print(pq.get())
print(pq.qsize())

#Imprime o primeiro elemento:
print(pq.get())
print(pq.qsize())

#Imprime o tamanho da fila:
print(pq.qsize())

#Uma diferença muito importatante entre Filas e Filas de prioridade é que as filas de prioridade organizam os elemento de forma crescente, indeferentes a ordem em que receberam os elementos. Por exemplo, se eu desse três put em uma fila de prioridade com os seguintes valores, respectivamente 3, 1 e 20, ela armazenaria 1, 3 e 20. A fila normal armazena as coisas de acordo com os puts(3, 1, 20) -> 3, 1, 20.