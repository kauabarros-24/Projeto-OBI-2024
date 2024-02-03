from queue import LifoQueue

#área de var
q = LifoQueue()
repeticoes = int(input("Digite o número de repetições: "))
lista = []

#Programa de apoio
for i in range(repeticoes):
    lista.append(input("Digite a sequência: "))

#Programa principal

for c in lista:
    q = LifoQueue()
    if len(c) % 2 != 0:
        print("N")
    else:
        for o in c:
            for j in c:
                if o == "[" and j == "]" or o == "(" and j == ")" or o == "{" and j == "}" :
                    q.put("S")
                    c.remive(o)
                    c.remove(j)
                else:
                    q.put("N")
        print(q.get())


    

    
