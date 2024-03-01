from queue import SimpleQueue
quantidadeConsultas, quantidadeVar = map(int, input().split())

lq = SimpleQueue()
lista = []

def merge(value):
    if value not in lista: lista.append(value)
def find(bnc1, bnc2):
    lq.put("S") if bnc1 and bnc2 in lista or bnc1 in lista or bnc2 in lista else lq.put("N")

for _ in range(quantidadeVar):
    tipoOp, banco1, banco2 = map(str, input().split())
    banco1 = int(banco1)
    banco2 = int(banco2)
    if tipoOp == "F":
        merge(banco1)
        merge(banco2) 
    else:
        find(banco1, banco2)
    
while lq.qsize() > 0: print(lq.get())