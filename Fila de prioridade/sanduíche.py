pedacos, tamanhoComer =  map(int, input().split())
tamanhoPedacos = list(map(int, input().split()))

i = 0
resp = 0

for mestre in tamanhoPedacos:
    i+=1
    contador = mestre
    for sudito in tamanhoPedacos[i:]:
        contador+=sudito
        if contador - sudito <= tamanhoComer and contador > tamanhoComer:    
            resp+=1
            break
    

print(pedacos - resp)
