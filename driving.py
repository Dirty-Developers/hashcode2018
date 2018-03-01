

class Ride(object):

    def __init__(self, id, sr, sc, er, ec, st, et):
        self.id = id
        self.start_point = (int(sr), int(sc))
        self.end_point = (int(er), int(ec))
        self.start_time = int(st)
        self.end_time = int(et)
        self.distance = abs(int(er)-int(sr)) + abs(int(ec)-int(sc))

    def __str__(self):
        return str(self.id)


class Car(object):
    def __init__(self):
        self.current_position = (0, 0)
        self.current_time = 0
        self.rides = []

    def assign_ride(self, ride):
        self.rides.append(ride)
        self.current_time += self.get_timelapse(ride) + ride.distance
        self.current_position = ride.end_point

    def get_timelapse(self, ride):
        distance = abs(ride.end_point[0]-self.current_position[0]) + abs(ride.end_point[1]-self.current_position[1])
        now = self.current_time + distance
        if ride.start_time > now:
            now += ride.start_time - now
        return now


if __name__ == '__main__':
    rides = []
    i = 0
    with open('inputs/a_example.in', 'r') as f:
        R, C, F, N, B, T = f.readline()[:-1].split(' ')
        for l in f.readlines():
            rides.append(Ride(i, *l[:-1].split(' ')))
            i += 1

    cars = [Car() for _ in range(F)]

    for r in rides:
        print("{} -> {}".format(r, r.reward))