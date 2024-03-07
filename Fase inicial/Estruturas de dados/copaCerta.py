from queue import SimpleQueue
vencedores = [[], [], [], [], []]

vencedores[0] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
q = SimpleQueue()

for fase in range(1, 5):
    for jogo in range(0, len(vencedores[fase - 1]), 2):
        equipe1 = vencedores[fase - 1][jogo]
        equipe2 = vencedores[fase - 1][jogo + 1] 
        gol1, gol2 = map(int, input().split())
        if gol1 > gol2:
            vencedores[fase].append(equipe1)
        else:
            vencedores[fase].append(equipe2)
print(vencedores[4][0])

        

        

