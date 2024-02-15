programa, versao = map(int, input().split())

repositorio = {}
resposta = {}

for _ in range(programa):
    nPrograma, nVersao = map(int, input().split())
    repositorio[nPrograma] = nVersao

for _ in range(versao):
    nPrograma, nVersao = map(int, input().split())
    if nPrograma not in repositorio:
        repositorio[nPrograma] = nVersao
        resposta[nPrograma] = nVersao
    elif repositorio[nPrograma] < nVersao:
        resposta[nPrograma] = nVersao
        repositorio[nPrograma] = nVersao

for programa in sorted(resposta):
    print(programa, resposta[programa])
        
