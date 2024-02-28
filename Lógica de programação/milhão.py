dias = int(input())
l = 0
contador = 0
for i in range(dias):
    soma = int(input())
    l+=soma
    if l < 1000000:
        contador+=1

print(contador + 1)
    


