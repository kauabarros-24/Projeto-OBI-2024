from queue import LifoQueue, SimpleQueue

#Var
while True:
    tamanhoN, sairD = map(int, input("Digite o tamanho do número e o valor a ser retirado: ").split())
    if tamanhoN == 0 and sairD == 0:
        break
    str = []
    str.append(int(input("Digite o número a ser usado: ")))


