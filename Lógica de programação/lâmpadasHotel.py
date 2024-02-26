#OBI 2016 1f
iA, iB, fA, fB = map(int, input().split())

if fB == iB:
    print(0) if iA == fA else print(1)
else:
    print(1) if iA != fA else print(2)
    

        
