from queue import LifoQueue

#área de var
q = LifoQueue()
repeticoes = int(input())
lista = []

#Programa de apoio
for i in range(repeticoes):
    lista.append(input())

#Programa principal

for c in lista:
    q = LifoQueue()
    if len(c) % 2 != 0:
        print("N")
    else:
        t = 1
        for o in c:
            print(f"Esse é o = {o}")
            for j in enumerate(c[t:]):
                if o == "[" and j == "]" or o == "(" and j == ")" or o == "{" and j == "}" :
                    q.put("S")
                    print(f"Esse é c antes do replace = {c}")
                    x = c.replace(o, "").replace(j, "")
                    c = x
                    print(f"Esse é c depois do replace = {c}")
                    t+=1
    
                else:
                    print("Caso não ativado")
                    t+=1
    
                    q.put("N")
        print(q.get())




    

    
