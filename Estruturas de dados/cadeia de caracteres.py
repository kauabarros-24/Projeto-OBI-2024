from queue import LifoQueue
#Área de var:
q = LifoQueue()
repeticoes = int(input("Digite o numéro de repetições: "))
lista = []
o = 0

#Receber ás var's:
for i in range(repeticoes):
    lista.append(input("Digite a expressão: "))

#Programa principal:    
for c in lista:
    if len(c) % 2 != 0:
        print("N")
    else:
        for j in c:
            for o in c:
                if j == "(" and o == ")" or j == "[" and o == "]" or j == "{" and o == "}":
                     q.put("S")
                else:
                    q.put("N")
        print(q.get())

            
    


    







    

    

    
