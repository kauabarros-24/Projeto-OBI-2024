from queue import SimpleQueue
import string

#ÁREA DE VAR'S
a = list(string.ascii_lowercase)
q = SimpleQueue()
listaOitavas = []
n = 1

#Adicionais:
for c in a:
    q.put(a)
    if q.qsize() == 16:
        break
print(q.qsize())
    
#Tratamento:
class Pontos:
    def __init__(self, resultado0, resultado1):
        self.resultado0 = resultado0
        self.resultado1 = resultado1

    while n <= 12:
        if n <= 8 :
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
        elif n >=9:
                def quartas(self):
                    if self.resultado0 > self.resultado1:
                        q.get(listaOitavas[1])
                        listaOitavas.remove(listaOitavas[1])
                        print(listaOitavas)
                    else:
                        q.get(listaOitavas[0])
                        listaOitavas.remove(listaOitavas[0])
                        print(listaOitavas)

#Programa principal:
for i in range(12):
    ##Pegar valores:
    resultado = input("Digite os valores da partida: ").split()
    pontos = Pontos(resultado[0], resultado[1])
    #pontos.oitavas()
    if i > 8:
        pontos.quartas()
    