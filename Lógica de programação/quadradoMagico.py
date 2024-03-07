#Pegar os dados
tamanho = int(input())
listaValores = [list(map(int, input().split())) for _ in range(tamanho)]

#Função para vericifar a soma e valores de apoio:
valor = 0
valorSublista = 0
count = 0
listaApoio = []
def testeSoma(valorSoma): return valorSoma == sum(listaValores[0])

#Verificar a soma na horizontal:
valor+= sum(1 for c in range(len(listaValores)) if testeSoma(sum(listaValores[c])))
#Vericar a soma na vertical:
i = 0

for sublista in listaValores:
    listaApoio.append(sublista[count])
    if len(listaApoio) == tamanho:
        count+=1
        print(listaApoio)
        testeSoma(sum(listaApoio))


    




