#Pegar os dados
tamanho = int(input())
listaValores = [list(map(int, input().split())) for _ in range(tamanho)]

#Função para vericifar a soma e valores de apoio:
valor = 0
valorSublista = 0
count = 0
listaDiagonal = []
listaD = []
def testeSoma(valorSoma): return valorSoma == sum(listaValores[0])

#Verificar a soma na horizontal:
valor+= sum(1 for c in range(len(listaValores)) if testeSoma(sum(listaValores[c])))
#Vericar a soma na vertical:
for c in range(len(listaValores)):
    somaColuna = sum(sublista[c] for sublista in listaValores)
    if testeSoma(somaColuna): pass
#Diagonal decrescente
contador = 0
for c in range(len(listaValores)):
    listaDiagonal.append(listaValores[c - 1][contador])
    contador+=1
#Diagonal crescente
contador = 0
for c in range(tamanho):
    listaD.append(listaValores[c - 1][contador])
    contador+=1

print(testeSoma(sum(listaDiagonal)))