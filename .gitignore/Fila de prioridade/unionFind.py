MAXN = 1000010

parent = [0] * MAXN
size = [0] * MAXN


def find(value):
    if parent[value] == value:
        return value
    parent[value] = find(parent[value])
    return parent[value]


def merge(i, j):
    i = find(i)
    j = find(j)

    if i == j:
        return

    if size[i] >= size[j]:
        parent[j] = i
        size[i] += size[j]
    else:
        parent[i] = j
        size[j] += size[i]


n, q = map(int, input().split())

for i in range(n):
    size[i] = 1
    parent[i] = i
    

for i in range(q):
    qtype, a, b = input().split()
    qtype = int(qtype)
    a = int(a)
    b = int(b)

    if qtype == 1:
        merge(a, b)
    else:
        if find(a) == find(b):
            print("Mesmo conjunto")
        else:
            print("Conjuntos diferentes")
