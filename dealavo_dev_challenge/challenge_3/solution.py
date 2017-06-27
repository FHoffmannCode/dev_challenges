with open('example.txt') as data:
    tourist_count = int(data.readline().strip())
    times = []
    for i in range(tourist_count):
        times.append(int(data.readline().strip()))

times_table = {1: times[0], 2: times[1], 3: times[0] + times[1] + times[2]}


def count_ith_time(i):
    times_table[i] = min((times_table[i - 2] + times[0] + 2 * times[1] + times[i - 1], times_table[i - 1] + times[0] + times[i - 1]))
    return times_table[i]

for i in range(4, tourist_count + 1):
    count_ith_time(i)
print times_table[tourist_count]

