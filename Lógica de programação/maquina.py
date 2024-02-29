andar3, andar2, andar1 = int(input()), int(input()), int(input())
#lista = [andar3, andar2, andar1]                      
#-> Solução do Kauã  
#maiorValor = max(lista)
#if maiorValor == andar3:
#    print((andar1 * 4) + (andar2 * 2))
#elif maiorValor == andar2:
    #print((andar1 * 2) + (andar3 * 2))
#else:
    #print((andar3) * 4 + (andar2 * 2))

um = andar3 * 4 + andar2 * 2
dois = andar3 * 2 + andar1 * 2
tres = andar1 * 4 + andar2 * 2
print(min(um, min(dois, tres)))


    


