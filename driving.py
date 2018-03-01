#!/usr/bin/env python
# -*- coding: utf-8 -*
from sys import argv


class Ride(object):

    def __init__(self, id, sr, sc, er, ec, st, et):
        self.id = id
        self.start_point = (int(sr), int(sc))
        self.end_point = (int(er), int(ec))
        self.start_time = int(st)
        self.end_time = int(et)
        self.__distance = abs(int(er)-int(sr)) + abs(int(ec)-int(sc))


    def __len__(self):
        return self.__distance

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self)

    def __cmp__(self, other):
        if self.start_time < other.start_time:
            return -1
        if self.start_time > other.start_time:
            return 1
        return 0


class Car(object):
    def __init__(self):
        self.current_position = (0, 0)
        self.current_time = 0
        self.rides = []

    def assign_ride(self, ride):
        self.rides.append(ride)
        self.current_time += self.get_timelapse(ride) + len(ride)
        self.current_position = ride.end_point

    def get_timelapse(self, ride):
        distance = abs(ride.start_point[0]-self.current_position[0]) + abs(ride.start_point[1]-self.current_position[1])
        now = self.current_time + distance
        if ride.start_time > now:
            now += ride.start_time - now
        return now

    def voyage_points(self, ride):
        bonus = 0
        if self.current_time + self.get_timelapse(ride) == ride.start_time:
            bonus = BONUS
        return len(ride) + bonus

    def voyage_ratio(self, ride):
        return float(self.voyage_points(ride))/(self.get_timelapse(ride) + len(ride))

    def __str__(self):
        return str(len(self.rides)) + ' ' + ' '.join([str(x) for x in self.rides])

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    rides = []
    i = 0
    with open(argv[1], 'r') as f:
        R, C, F, N, BONUS, T = (int(x) for x in f.readline()[:-1].split(' '))
        for l in f.readlines():
            rides.append(Ride(i, *l[:-1].split(' ')))
            i += 1

    cars = [Car() for _ in range(F)]
    assigned_cars = []
    assigned_rides = {}

    rides.sort()

    for r in rides:
        t = min([a.current_time for a in cars])
        if assigned_rides.has_key(r.id):
            continue
        best_car = None
        best_ratio = 0
        for c in cars:
            ratio = c.voyage_ratio(r)
            if ratio > best_ratio and t >= c.current_time:
                best_ratio = ratio
                best_car = c
        if best_car:
            best_car.assign_ride(r)
            assigned_rides[r.id] = True

    print('\n'.join([str(c) for c in cars]))
