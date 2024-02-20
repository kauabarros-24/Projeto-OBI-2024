pedacos, tamanhoPedaco = map(int, input().split())
seq = list(map(int, input().split()))

contador = 0
for c in range(pedacos):
    for j in range(c, pedacos):
        if sum(seq[c:c+1]) <= tamanhoPedaco:
            contador+=1

for c in range(pedacos - 1):
    for j in range(c + 1,  pedacos):
        if sum(tamanhoPedaco[:c]) + sum(tamanhoPedaco[j:]) == tamanhoPedaco:
            contador+=1

print(contador)
