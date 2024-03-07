#Pegar os dados
tamanho = int(input())
listaValores = [list(map(int, input().split())) for _ in range(tamanho)]

#Função para vericifar a soma e valores de apoio:
valor = 0
valorSublista = 0
count = 0
def testeSoma(valorSoma): return valorSoma == sum(listaValores[0])

#Verificar a soma na horizontal:
valor+= sum(1 for c in range(len(listaValores)) if testeSoma(sum(listaValores[c])))
#Vericar a soma na vertical:
for c in range(len(listaValores)):
    somaColuna = sum(sublista[c] for sublista in listaValores3)
    if testeSoma(somaColuna):
        count+=1
#




    




