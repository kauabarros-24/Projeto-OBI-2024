from queue import SimpleQueue
quantidadeConsultas, quantidadeVar = map(int, input().split())

lq = SimpleQueue()
lista = []

def find_root(value): return value in lista
    
def merge(x, y):
    x_root = find_root(x)
    y_root = find_root(y)
    if x_root == False: lista.append(x)
    if y_root == False: lista.append(y)

def find(x, y):
    x_root = find_root(x)
    y_root = find_root(y)
    lq.put("S") if y_root == True or x_root == True else lq.put("N")
    
for _ in range(quantidadeVar):
    tipoOp, banco1, banco2 = input().split()
    banco1, banco2 = int(banco1), int(banco2)
    merge(banco1, banco2) if tipoOp == "F" else find(banco1, banco2)
    
while lq.qsize() > 0: print(lq.get())