with open('lot1a.in') as data:
    station_count = int(data.readline().strip())
    fuels = []
    distances = []
    for _ in range(station_count):
        station_data = [int(num) for num in data.readline().strip().split()]
        fuels.append(station_data[0])
        distances.append(station_data[1])
is_ok = ['NIE' for _ in range(station_count)]


def find_first_viable_station_left():
    station = 0
    fuel = 0
    min_fuel = 0
    for i in range(station_count):
        fuel += fuels[i] - distances[i]
        if fuel < min_fuel:
            station = i + 1
            min_fuel = fuel
    if fuel < 0:
        return False
    if station == station_count:
        station = 0
    sum_fuel = 0
    is_ok[station] = 'TAK'
    for i in range(station - 1, -1, -1):
        sum_fuel += fuels[i] - distances[i]
        if sum_fuel >= 0:
            is_ok[i] = 'TAK'
            sum_fuel = 0
    for i in range(station_count - 1, station, -1):
        sum_fuel += fuels[i] - distances[i]
        if sum_fuel >= 0:
            is_ok[i] = 'TAK'
            sum_fuel = 0
    return True


def find_first_viable_station_prawo():
    station = 0
    fuel = fuels[0] - distances[station_count - 1]
    min_fuel = 0
    if fuel < min_fuel:
        min_fuel = fuel
        station = station_count - 1
    for i in range(station_count - 1, 0, -1):
        fuel += fuels[i] - distances[i - 1]
        if fuel < min_fuel:
            station = i - 1
            min_fuel = fuel
    sum_fuel = 0
    is_ok[station] = 'TAK'
    for i in range(station + 1, station_count):
        sum_fuel += fuels[i] - distances[i - 1]
        if sum_fuel >= 0:
            is_ok[i] = 'TAK'
            sum_fuel = 0
    sum_fuel += fuels[0] - distances[station_count - 1]
    if sum_fuel >= 0:
        is_ok[0] = 'TAK'
        sum_fuel = 0
    for i in range(1, station):
        sum_fuel += fuels[i] - distances[i - 1]
        if sum_fuel >= 0:
            is_ok[i] = 'TAK'
            sum_fuel = 0

if find_first_viable_station_left():
    find_first_viable_station_prawo()
print is_ok
