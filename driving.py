

class Ride(object):

    def __init__(self, id, sr, sc, er, ec, st, et):
        self.id = id
        self.start_point = (sr, sc)
        self.end_point = (er, ec)
        self.start_time = st
        self.end_time = et

    def __str__(self):
        return str(self.id)


if __name__ == '__main__':
    rides = []
    i = 0
    with open('inputs/a_example.in', 'r') as f:
        R, C, F, N, B, T = f.readline()[:-1].split(' ')
        for l in f.readlines():
            rides.append(Ride(i, *l[:-1].split(' ')))
            i += 1

    for r in rides:
        print(r)