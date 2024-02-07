#Vetore dinâmicos
v = [1, 2, 3]

#Retorna o tamanho da lista
print(f"O tamanho do vetor é {len(v)}")

#Inserir um elemento no final do vetor:
v.append(4)
print(f"Esses são os elementos do vetor: {v}")

#Deletar um elemento no final do vetor:
print(f"O elemento {v.pop} foi deletado do vetor 'v'")

#O comando insert insere um elemento em uma posição específica, onde dizemos, primeiramente a posição do elemento e em seguida o elemento que vamos inserir:
#Abaixo, inserimos o elemento 1 na posição 0:
v.insert(0, 1)
print(f"Esse é o vetor depois da expansão: {v}")

#Remove o primeiro elemento da lista de um valor específico da lista:
#Removemos o primeiro valor "2" da lista:
v.remove(2)
print(f"Esse é 'v' depois da remoção: {v}")

#Zera a lista:
v.clear()
print(f"Após zerarmos o vetor, seu tamanho é: {len(v)}")