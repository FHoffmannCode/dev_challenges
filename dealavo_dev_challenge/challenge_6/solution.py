res = 0
w = 0

with open('met6b.in') as data:
    n, l = tuple([int(number) for number in data.readline().strip().split()])
    warstwa = [0 for _ in range(n)]
    kto = [0 for _ in range(n)]
    ile = [0 for _ in range(n)]
    for _ in range(n - 1):
        a, b = tuple([int(number) for number in data.readline().strip().split()])
        a -= 1
        b -= 1
        ile[a] += 1
        kto[a] += b
        ile[b] += 1
        kto[b] += a


for i in range(n):
    if ile[i] == 1:
        warstwa[w] = i
        w += 1
while w > 0:
    res += min([2 * l, w])
    nw = 0
    for i in range(w):
        x = warstwa[i]
        kto[kto[x]] -= x
        ile[kto[x]] -= 1
        if ile[kto[x]] == 1:
            warstwa[nw] = kto[x]
            nw += 1
    w = nw

print res