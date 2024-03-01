# Criando um set usando o construtor
s = set()

# Outra forma de criar um set, já inicializando com os elementos 1, 2 e 3
s = {1, 2, 3}

# Adiciona um elemento ao set
s.add(1)

# Remove um elemento do set
s.remove(1)

# Imprime o primeiro elemento do set, equivalente ao begin() do c++
print(next(iter(s)))

# Verifica se o elemento 1 está no set
print(1 in s)

# Itera sobre todos os elementos do set
for e in s:
    print(e)
