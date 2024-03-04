z = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

def quadrante(x, y, z):
    if x > z/2 and y > z/2:
        return 1
    elif x <= z/2 and y > z/2:
        return 2
    elif x <= z/2 and y <= z/2:
        return 3
    else:
        return 4
   
if quadrante(x1, y2, z) ==  quadrante(x2, y2, z):
    print("N")
else:
    print("S")