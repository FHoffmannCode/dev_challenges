class Node():
    def __init__(self, distance, process):
        self.distance = distance
        self.process = process

    def __gt__(self, other):
        return self.distance > other.distance

    def __lt__(self, other):
        return self.distance < other.distance