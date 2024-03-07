#Pegar os dados
tamanho = int(input())
listaValores = [list(map(int, input().split())) for _ in range(tamanho)]

#Função para vericifar a soma e valores de apoio:
valor = 0
def testeSoma(valorSoma):
    global valor
    if valorSoma == sum(listaValores[0]):
        valor+=1
soma = 0
print(valor)
#Verificar a soma na horizontal:
testeSoma(sum(listaValores[c]) for c in range(len(listaValores)))