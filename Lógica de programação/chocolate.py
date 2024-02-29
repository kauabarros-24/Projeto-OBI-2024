import math
medida, coordenadas1, coordenadas2 = int(input()), list(map(int, input().split())), list(map(int, input().split()))

if coordenadas1[0] + (medida / 2 - 1) == coordenadas2[0] - (medida / 2) or coordenadas1[0] - (math.ceil(medida / 2) * -1) == coordenadas2[0] - math.ceil(coordenadas2[1]):
    print("S")
else:
    print("N")

    


 