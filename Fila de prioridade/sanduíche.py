pedacos, tamanhoPedacos = map(int, input().split())
seq = list(map(int, input().split()))


contador = 0

#for i in range(pedacos):
  #  for j in range(i, pedacos):
  #      if sum(seq[i+1:j+1]) <= tamanhoPedacos:
   #         contador+=1
    #        break

for i in range(pedacos):
    for j in range(i+1, pedacos):
        if sum(seq[:i]) + sum(seq[j:]) == 0:
            contador+=1
            




print(contador)