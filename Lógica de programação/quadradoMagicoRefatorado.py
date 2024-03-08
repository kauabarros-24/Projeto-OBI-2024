#Pegar os dados
tamanho = int(input())
listaValores = [list(map(int, input().split())) for _ in range(tamanho)]

#Função de soma de variáveis de apoio:
def testeSoma(valorSoma): return valorSoma == sum(listaValores[0])
somaVertical, somaHorizontal, somaDiagonalC = 0, 0, []

#vertical:
somaVertical+= sum(1 for c in range(len(listaValores)) if testeSoma(sum(listaValores[c])))
#Horizontal:
somaHorizontal+= sum(1 for c in range(len(listaValores)) if testeSoma(listaValores[c - 1][c - 1]))

