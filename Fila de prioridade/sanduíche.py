N, D = map(int, input().split())
A = list(map(int, input().split()))

ans1 = 0
l = 0
r = 0
soma = 0

while l < N:
    while r < N and soma + A[r] <= D:
        soma += A[r]
        r += 1

    if soma == D:
        ans1 += 1

    soma -= A[l]
    l += 1

Pref = [0] * N
Suf = [0] * N

acc = 0
for i in range(N):
    acc += A[i]
    Pref[i] = acc

acc = 0
for i in range(N - 1, -1, -1):
    acc += A[i]
    Suf[i] = acc

ans2 = 0
SufCount = {}

for i in range(N - 2, -1, -1):
    if Suf[i + 1] not in SufCount:
        SufCount[Suf[i + 1]] = 0

    SufCount[Suf[i + 1]] += 1

    if Pref[i] > D:
        continue

    if (D - Pref[i]) in SufCount:
        ans2 += SufCount[D - Pref[i]]

print(ans1 + ans2)
