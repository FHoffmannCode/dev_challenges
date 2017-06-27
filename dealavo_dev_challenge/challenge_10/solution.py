import collections

tmin = []
tmax = []
with open('tem11a.in') as data:
    n = int(data.readline().strip())
    for _ in range(n):
        temps = data.readline().strip().split()
        tmin.append(int(temps[0]))
        tmax.append(int(temps[1]))

Q = collections.deque()
wynik = 0
for i in range(n):
    a, b = tmin[i], tmax[i]
    naj = i
    while len(Q) != 0 and Q[0][1] >= a:
        naj = min([naj, Q[0][0]])
        Q.popleft()
    Q.appendleft((naj, a))
    while len(Q) != 0 and Q[-1][1] > b:
        wynik = max([wynik, i - Q[-1][0]])
        Q.pop()
while len(Q) != 0:
    wynik = max([wynik, n - Q[-1][0]])
    Q.pop()
print wynik
