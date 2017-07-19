from dealavo_dev_challenge.challenge import Challenge


class Challenge_4(Challenge):

    def solve_challenge(self, filename):
        with open(filename) as data:
            station_count = int(data.readline().strip())
            fuels = []
            distances = []
            for _ in range(station_count):
                station_data = [int(num) for num in data.readline().strip().split()]
                fuels.append(station_data[0])
                distances.append(station_data[1])
        is_ok = ['NIE' for _ in range(station_count)]

        def seek_left():
            cur_fuel = 0
            station = 0
            min_fuel = 0
            station = 0
            for i in range(station_count):
                cur_fuel += fuels[i] - distances[i]
                if cur_fuel < min_fuel:
                    station = i + 1
                    min_fuel = cur_fuel
            if cur_fuel < 0:
                return False
            if station == station_count:
                station = 0
            is_ok[station] = 'TAK'
            cur_fuel = 0
            for i in range(station - 1, -1, -1):
                cur_fuel += fuels[i] - distances[i]
                if cur_fuel >= 0:
                    is_ok[i] = 'TAK'
                    cur_fuel = 0
            for i in range(station_count - 1, station, -1):
                cur_fuel += fuels[i] - distances[i]
                if cur_fuel >= 0:
                    is_ok[i] = 'TAK'
                    cur_fuel = 0
            return True

        def seek_right():
            cur_fuel = fuels[0] - distances[station_count - 1]
            min_fuel = 0
            station = 0
            if cur_fuel < min_fuel:
                station = station_count - 1
                min_fuel = cur_fuel
            for i in range(station_count - 1, 0, -1):
                cur_fuel += fuels[i] - distances[i - 1]
                if cur_fuel < min_fuel:
                    station = i - 1
                    min_fuel = cur_fuel
            if cur_fuel < 0:
                return False
            is_ok[station] = 'TAK'
            cur_fuel = 0
            for i in range(station + 1, station_count):
                cur_fuel += fuels[i] - distances[i - 1]
                if cur_fuel >= 0:
                    is_ok[i] = 'TAK'
                    cur_fuel = 0
            cur_fuel += fuels[0] - distances[station_count - 1]
            if cur_fuel >= 0:
                is_ok[0] = 'TAK'
                cur_fuel = 0
            for i in range(1, station):
                cur_fuel += fuels[i] - distances[i - 1]
                if cur_fuel >= 0:
                    is_ok[i] = 'TAK'
                    cur_fuel = 0
            return True
        if seek_left():
            seek_right()
        return is_ok



    @staticmethod
    def compare_res_with_out(res, out):
        proc_out = out.strip().split()
        return res == proc_out

    @staticmethod
    def res_to_str(res):
        return res
