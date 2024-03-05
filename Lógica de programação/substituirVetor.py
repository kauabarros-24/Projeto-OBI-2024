#Ler 10 valores inteiros
listaValores = [int(input())for _ in range(10)]

#Imprimir o menor valor:
menorValor = min(listaValores)
print("Menor:",menorValor)

#Pegar os índices na qual listaValores[0] estiver e substituir por -1:
listaOcorrencias = []
for i, c in enumerate(listaValores):
    if c == menorValor:
        listaOcorrencias.append(i)
        listaValores[i] = -1
        
#Imprimir:
print("Ocorrencias:",*listaOcorrencias)
print(*listaValores)