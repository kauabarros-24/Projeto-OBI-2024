caixas = []
for _ in range(3): caixas.append(int(input()))
caixas.sort()
print(1) if caixas[2] > caixas[0] + caixas[1] or caixas[2] > caixas[1] > caixas[0] else(print(2) if caixas[2] == caixas[0] + caixas[1] or caixas[1] == caixas[2] and caixas[0] < caixas[1] or caixas[2] > caixas[1] and caixas[0] == caixas[1] else print(3))