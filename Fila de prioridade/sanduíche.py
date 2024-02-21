from queue import SimpleQueue
#pedacos, tamanhoPedaco = map(int, input().split())
#seq = list(map(int, input().split()))

#contador = 0
#for c in range(pedacos):
##for j in range(c, pedacos):
###if sum(seq[c:c+1]) <= tamanhoPedaco:
####contador += 1

#for c in range(pedacos - 1):
##for j in range(c + 1,  pedacos):
###if sum(tamanhoPedaco[:c]) + sum(tamanhoPedaco[j:]) == tamanhoPedaco:
####contador += 1

#print(contador)

pedacos , tamanhoPedaco = map(int, input().split())
seq = list(map(int, input().split()))

contador = 0
lista = []
for c in range(pedacos):
    for j in range(c, pedacos):
        soma = sum(seq[c:j+1])
        lista.append(soma)
        if soma > tamanhoPedaco and lista[-1] <= tamanhoPedaco:
            contador+=1 
            print(soma)
            soma = 0
            break
        

lista.clear()
for c in range(pedacos - 1):
    for j in range(c+1, pedacos):
        soma = sum(seq[:c]) + sum(seq[j:])
        lista.append(soma)
        if soma > tamanhoPedaco and lista[-1] <= soma:
            contador+=1
            print(soma)
            soma = 0
            break
        
print(contador)

