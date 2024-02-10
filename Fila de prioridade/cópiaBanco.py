contador20 = 0

with open("input.txt", "r") as file:
    lines = file.readlines()
    quantidadeCaixas, numeroClientes = map(int, lines[0].split())

    lista = []
    for line in lines[1:]:
        tempoChegada, tempoAtendimento = map(int, line.split())
        lista.append((tempoChegada, tempoAtendimento))

if quantidadeCaixas == 1:
    for i, c in lista:
        todosAtendimentos = i
        break
    for chegada, atendimento in lista:
        print(f"chegada: {chegada} | atendimento: {atendimento}")
        ate = todosAtendimentos - chegada
        todosAtendimentos += atendimento
        print(f"ate: {ate} | todosAtendimentos: {todosAtendimentos}")
        if ate > 20:
            contador20 += 1
            print(f"Contador: {contador20}")
        if chegada > ate:
            tempoAtendimento, ate = 0, 0
            print("Zerados")
        print(" ")
else:
    for c in range(quantidadeCaixas):
        todosAtendimentos = lista[c - 1]
        for i, c in lista[c - 1:]:
            todosAtendimentos = i
            break
        for chegada, atendimento in lista[c-1::quantidadeCaixas]:
            ate = todosAtendimentos - chegada
            todosAtendimentos += atendimento
            if ate > 20:
                contador20 += 1
            if chegada > ate:
                tempoAtendimento, ate = 0, 0

print(contador20)



        


    
