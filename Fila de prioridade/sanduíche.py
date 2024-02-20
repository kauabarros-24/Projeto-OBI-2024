pedacos, tamanhoPedaco = map(int, input().split())
seq = list(map(int, input().split()))

contador = 0
for c in range(pedacos):
    for i in range(i, pedacos):
        if sum(seq[c:i+1]) <= tamanhoPedaco:
            contador+=1

for c in range(pedacos):
    for j in range(i + 1,  pedacos):
        if sum(tamanhoPedaco[:i]) + sum(tamanhoPedaco[j:]) == tamanhoPedaco:
            contador+=1

print(contador)
