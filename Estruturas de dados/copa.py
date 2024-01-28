from queue import SimpleQueue
import string

# ÁREA DE VARIAVEIS
a = list(string.ascii_lowercase)
q = SimpleQueue()
listaOitavas = []
listaQuartas = []
listaSemi = []
n = 1

#Extra:
for i in a:
    q.put(i)
print(q.qsize())

#Tratamento
class Pontos:
    def __init__(self, resultado0, resultado1):
        self.resultado0 = resultado0
        self.resultado1 = resultado1
    while n <= 14:
        if n <= 8:
            def oitavas(self):
                if self.resultado0 > self.resultado1:
                    q.get(a[1])
                    listaOitavas.append(a[0])
                    a.remove(a[0])
                    a.remove(a[0])
                else:
                    q.get(a[0])
                    listaOitavas.append(a[1])
                    a.remove(a[0])
                    a.remove(a[0])
                print(listaOitavas)
        elif n <= 12:
            def quartas(self):
                if self.resultado0 > self.resultado1:
                    q.get(listaOitavas[1])
                    listaQuartas.append(listaOitavas[0])
                    listaOitavas.remove(listaOitavas[0])
                    listaOitavas.remove(listaOitavas[0])
                else:
                    q.get(listaOitavas[0])
                    listaQuartas.append(listaOitavas[1])
                    listaOitavas.remove(listaOitavas[0])
                    listaOitavas.remove(listaOitavas[0])
                print(listaQuartas)
        elif n <= 14:
            def semi(self):
                if self.resultado0 > self.resultado1:
                    q.get(listaQuartas[1])
                    listaSemi.append(listaQuartas[0])
                    listaQuartas.remove(listaQuartas[0])
                    listaQuartas.remove(listaQuartas[0])
                    print(listaSemi)
                else:
                    q.get(listaQuartas[0])
                    listaSemi.append(listaQuartas[1])
                    listaQuartas.remove(listaQuartas[0])
                    listaQuartas.remove(listaQuartas[0])
                    print(listaSemi)
                print(listaSemi)
        n+=1

#Programa principal

for i in range(14):
    resultado = input("Digite os valores: ").split()
    pontos = Pontos(resultado[0], resultado[1])
    if i < 8:
        pontos.oitavas()
    elif i < 12:
        pontos.quartas()
    elif i < 14:
        pontos.semi()
