with open("input2.txt", "r") as file:
    lines = file.readlines()
    quantidadeCaixas, numeroClientes = map(int, lines[0].split())

    lista = []
    for line in lines[1:]:
        sublista = []
        tempoChegada, tempoAtendimento = map(int, line.split())
        sublista.append(tempoChegada)
        sublista.append(tempoAtendimento)
        lista.append(sublista)
        
print(lista)

contador20 = 0
if quantidadeCaixas == 1:
    tempoAtendimento = lista[0][0]
    for chegada, atendimento in lista:
        espera = tempoAtendimento - chegada
        tempoAtendimento+=atendimento
        if espera > 20:
            contador20+=1
        if chegada > espera:
            espera, tempoAtendimento = 0, 0
else:
    for c in range(quantidadeCaixas):
        tempoAtendimento = lista[c - 1][0]
        print(f"Esse é o tempo de atendimento inicial: {tempoAtendimento}")
        for chegada, atendimento in lista[c - 1::quantidadeCaixas]:
            print(f"Chegada: {chegada}|Atendimento: {atendimento}")
            espera = tempoAtendimento - chegada
            print(f"Espera: {espera}")
            tempoAtendimento+=atendimento
            print(f"TempoAtendimento incrementado: {tempoAtendimento}")
            if espera > 20:
                contador20+=1
                print(f"Alguém esperou demais: {contador20}")
            if chegada > espera:
                espera, tempoAtendimento = 0, 0
                print("Zerado")
            print(" ")
            

print(contador20)

        
