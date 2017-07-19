import collections

tmin = []
tmax = []
with open('tem1ocen.in') as data:
    n = int(data.readline().strip())
    for _ in range(n):
        temps = data.readline().strip().split()
        tmin.append(int(temps[0]))
        tmax.append(int(temps[1]))

Q = collections.deque()

def dodej(wartosc, pozycja):
    while len(Q) > 0 and Q[0][0] <= wartosc:
        Q.popleft()
    Q.appendleft((wartosc, pozycja))


def wypiehdol(pozycja):
    if Q[-1][1] <= pozycja:
        Q.pop()


def magzimum():
    if len(Q) == 0:
        return -float('inf')
    return Q[-1][0]


wynik = 0
j = 0
for i in range(n):
    a, b = tmin[i], tmax[i]
    while j < n and magzimum() <= tmax[j]:
        dodej(tmin[j], j)
        j += 1
    wynik = max([wynik, j - i])
    wypiehdol(i)
print wynik


