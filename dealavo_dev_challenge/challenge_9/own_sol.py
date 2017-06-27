with open('klo10.in') as data:
    n, m = tuple(data.readline().strip().split())
    heights = [int(num) for num in data.readline().strip().split()]
    k_table = [int(num) for num in data.readline().strip().split()]
m = int(m)
n = int(n)


def count(k):
    sh = [0]
    for i in range(n):
        sh.append(sh[i] + heights[i] - k)
    pref = []
    b = float('inf')
    for i in range(n):
        if b > sh[i]:
            pref.append(i)
            b = sh[i]
    suff = []
    b = - float('inf')
    for i in range(n, -1, -1):
        if b < sh[i]:
            suff.append(i)
            b = sh[i]
    c = len(suff) - 1
    best = 0
    for i in range(len(pref)):
        while c > 0 and sh[suff[c]] >= sh[pref[i]]:
            c -= 1
        c += 1
        if c < len(suff) and sh[suff[c]] >= sh[pref[i]] and best < suff[c] - pref[i]:
            best = suff[c] - pref[i]
    return best
print count(k_table[3])
