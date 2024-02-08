import time

atendente, pessoas = map(int, input("Digite o número de atendentes e o número de pessoas: ").split())

lista = []
for i in range(pessoas):
    subLista = []
    horaChegada, tempoAtendimento = map(int, input("Digite a sua hora de chegada e o tempo que durou o atendimento: ").split())
    subLista.append(horaChegada)
    subLista.append(tempoAtendimento)
    lista.append(subLista)

print(lista)

i, contadorPessoasFora, inicioAtendimento = 0, 0, 0
lista.append

if atendente == 1:
    che = 0 
    for chegada, atendimento in lista:
        print(f"Esses são os valores de chegada: {chegada} e de atendimento: {atendimento}")
        
        s = atendimento + inicioAtendimento
        print(f"Esse é o valor para incrementar: {s}")
        inicioAtendimento+=s
        print(inicioAtendimento)
        if chegada > inicioAtendimento:
            inicioAtendimento = 0
            print("Zerado")
        elif inicioAtendimento > 20:
            contadorPessoasFora+=1
            print(f"Esse é o contador: {contadorPessoasFora}")
        
    
else:
    for chegada, atendimento in lista[i::atendente]:
        s = chegada + atendimento
        inicioAtendimento+=s
        if chegada > inicioAtendimento:
            inicioAtendimento = 0
        elif inicioAtendimento > 20:
            contadorPessoasFora+=1   
    i+=1
print(contadorPessoasFora)

    
