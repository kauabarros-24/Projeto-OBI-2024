quantidadeCaixas, numeroClintes = map(int, input().split())

lista = []
for _ in range(numeroClintes):
    sublista = []
    tempoChegada, tempoAtendimento = map(int, input().split())
    sublista.append(tempoChegada)
    sublista.append(tempoAtendimento)
    lista.append(sublista)

contador20 = 0
if quantidadeCaixas == 1: 
    for i, c in lista:
            todosAtendimentos = i
            break
    for chegada, atendimento in lista:
        print(f"Esse é o valor de chegada: {chegada}")
        print(f"Esse é o valor de atendimento: {atendimento}")
        ate = todosAtendimentos - chegada
        
        if ate > 20:
            contador20+=1
           
        if chegada > ate:
            tempoAtendimento, ate = 0, 0
         
            
           
else:
    for c in range(quantidadeCaixas):
        for i, t in lista[c - 1:-1]:
            todosAtendimentos = i
            break
        for chegada, atendimento in lista[c-1::quantidadeCaixas]:
            ate = todosAtendimentos - chegada
            todosAtendimentos+= atendimento
            if ate > 20:
                contador20+=1
            if chegada > ate:
                tempoAtendimento, ate = 0, 0

print(contador20)
        


        


    
