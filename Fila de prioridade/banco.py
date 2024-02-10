
quantidadeCaixas, numeroClintes = map(int, input("Digite o número de caixas e o número de clientes: ").split())

lista = []
for _ in range(numeroClintes):
    sublista = []
    tempoChegada, tempoAtendimento = map(int, input("Digite o tempo de chegada e o tempo de atendimento: ").split())
    sublista.append(tempoChegada)
    sublista.append(tempoAtendimento)
    lista.append(sublista)

contador20 = 0
if quantidadeCaixas == 1: 
    valorAtendimentoAnteriores = 0
    todosAtendimentos = 0
    for chegada, atendimento in lista:
        ate = todosAtendimentos - chegada
        todosAtendimentos+= atendimento
        if ate > 20:
            contador20+=1
            print(contador20)
else:
    for c in range(quantidadeCaixas):
        valorAtendimentoAnteriores = 0
        todosAtendimentos = 0
        for chegada, atendimento in lista[c - 1:: quantidadeCaixas]:
            ate = todosAtendimentos - chegada
            todosAtendimentos+= atendimento
            if ate > 20:
                contador20+=1
                print(contador20)
        


        


    
