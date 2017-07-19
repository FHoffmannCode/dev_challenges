with open('example.in') as data:
    station_count = int(data.readline().strip())
    fuels = []
    distances = []
    for _ in range(station_count):
        station_data = [int(num) for num in data.readline().strip().split()]
        fuels.append(station_data[0])
        distances.append(station_data[1])
is_ok = ['NIE' for _ in range(station_count)]


def find_stations_left():
    fuel = 0
    min_fuel = 0
    station = 0
    for i in range(station_count):
        fuel += fuels[i] - distances[i]
        if fuel < min_fuel:
            station = i + 1
            min_fuel = fuel
    if fuel < 0:
        return False
    if station == station_count:
        station = 0
    is_ok[station] = 'TAK'
    fuel = 0
    for i in range(station - 1, -1, -1):
        fuel += fuels[i] - distances[i]
        if fuel >= 0:
            is_ok[i] = 'TAK'
            fuel = 0
    for i in range(station_count - 1, station, -1):
        fuel += fuels[i] - distances[i]
        if fuel >= 0:
            is_ok[i] = 'TAK'
            fuel = 0
    return True


def find_stations_right():
    min_fuel = 0
    station = 0
    fuel = fuels[0] - distances[station_count - 1]
    if fuel < min_fuel:
        min_fuel = fuel
        station = station_count - 1
    for i in range(station_count - 1, 0, -1):
        fuel += fuels[i] - distances[i - 1]
        if fuel < min_fuel:
            min_fuel = fuel
            station = i - 1
    is_ok[station] = 'TAK'
    fuel = 0
    for i in range(station + 1, station_count):
        fuel += fuels[i] - distances[i - 1]
        if fuel >= 0:
            is_ok[i] = 'TAK'
            fuel = 0
    fuel += fuels[0] - distances[station_count - 1]
    if fuel >= 0:
        is_ok[0] = 'TAK'
        fuel = 0
    for i in range(1, station):
        fuel += fuels[i] - distances[i - 1]
        if fuel >= 0:
            is_ok[i] = 'TAK'
            fuel = 0
    return True

if find_stations_left():
    find_stations_right()
print is_ok

