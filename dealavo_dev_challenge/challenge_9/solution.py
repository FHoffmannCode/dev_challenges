with open('klo10.in') as data:
    n, m = tuple(data.readline().strip().split())
    heights = [int(num) for num in data.readline().strip().split()]
    k_table = [int(num) for num in data.readline().strip().split()]
m = int(m)
n = int(n)


def count(k):
    sh = [0]
    pre = [0 for _ in range(n + 1)]
    suf = [0 for _ in range(n + 1)]
    for i in range(n):
        sh.append(sh[i] + heights[i] - k)
    pc = sc = 0
    b = float('inf')
    for i in range(n + 1):
        if b > sh[i]:
            pre[pc] = i
            pc += 1
            b = sh[i]
    b = -float('inf')
    for i in range(n, -1, -1):
        if b < sh[i]:
            suf[sc] = i
            sc += 1
            b = sh[i]
    c = sc - 1
    best = 0
    for i in range(pc):
        while c >= 0 and sh[suf[c]] >= sh[pre[i]]:
            c -= 1
        if c + 1 < sc and sh[suf[c + 1]] >= sh[pre[i]] and best < suf[c + 1] - pre[i]:
            best = suf[c + 1] - pre[i]
    return best
print count(k_table[3])
