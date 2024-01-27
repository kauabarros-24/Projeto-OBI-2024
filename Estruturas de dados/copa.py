from queue import SimpleQueue
import string

a = list(string.ascii_lowercase)
q = SimpleQueue()
listaResult = []
o = 0
listaVencedores = []

for c in a:
    q.put(c)
    o+=1
    if o == 16:
        break

#Programa principal:

for i in range(8):
    #Pegamos os resultados
    resultado = input("Digite o resultado do jogo: ").split()
    #Ordenamos eles
    for n in resultado:
        listaResult.append(n)
    #Colocamos na fila, separando-os em listas:
    if listaResult[0] > listaResult[1]:
        q.get(a[1])
        listaVencedores.append(a[0])
        a.remove(a[0])
        a.remove(a[0])
        print(listaVencedores)

    else:
        q.get(a[0])
        listaVencedores.append(a[1])
        a.remove(a[0])
        a.remove(a[0])
        print(listaVencedores)
        

print(q.qsize())
print(a)



    
       
    
    

