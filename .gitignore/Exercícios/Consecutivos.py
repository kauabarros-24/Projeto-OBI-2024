s = int(input())
l = []
pontos = 0
for c in range(1):
    seq = str(input().split())


pontos = 0
gambiarra = seq[0]
listaPontos = []
for c in seq:
    if gambiarra == c:
        listaPontos.append(pontos)
        pontos+=1
        print()
        print(c, pontos, "\n")
    else:
        gambiarra = c
        listaPontos.append(pontos)
        pontos = 0
        print(c, pontos, "\n")

listaPontos.sort()
print(listaPontos[-1])