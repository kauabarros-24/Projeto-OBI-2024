while True:
    tamanhoN, retirarD = map(int, input().split())
    if tamanhoN == 0 and retirarD == 0:
        break
    a, num, subnum = str(input()), [], []
    for c in a:
        num.append(c)
        subnum.append(c)
    subnum.sort()    
    for o in subnum:
        num.remove(o)
        if tamanhoN - retirarD == len(num):
            break
        
    resp =  ''.join(map(str, num))
    print(resp)
    

    


    




