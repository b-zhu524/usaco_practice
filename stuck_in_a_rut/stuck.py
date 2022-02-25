class Cow:
    def __init__(self, cow_id, direction, start_x, start_y):
        self.cow_id = cow_id
        self.dir = direction
        self.start_x = start_x
        self.start_y = start_y
        self.x = start_x
        self.y = start_y
        self.stuck = False

    def update_position(self, dist):
        if self.stuck:
            return
        if self.dir == "E":
            self.x = dist + self.start_x
        else:
            self.y = dist + self.start_y

    def report_result(self):
        if not self.stuck:
            return "Infinity"
        if self.dir == "E":
            return str(self.x - self.start_x)
        else:
            return str(self.y - self.start_y)


class Event:
    def __init__(self, nc, ec):
        self.x = nc.x
        self.y = ec.y
        self.c1 = nc
        self.c2 = ec
        self.t1 = self.y - self.c1.y
        self.t2 = self.x - self.c2.x
        if self.t1 > self.t2:
            self.c1, self.c2 = self.c2, self.c1
            self.t1, self.t2 = self.t2, self.t1

    def __lt__(self, other):
        if self.t2 != other.t2:
            return self.t2 < other.t2
        return self.t1 < other.t1


def solve2(n, cows_input):
    cows = []
    for i in range(n):
        d, x, y = cows_input[i]
        cows.append(Cow(i, d, x, y))

    events = []
    for nc in cows:
        if nc.dir != "N":
            continue
        for ec in cows:
            if ec.dir != "E":
                continue
            if nc.x < ec.x or ec.y < nc.y:
                continue
            event = Event(nc, ec)
            events.append(event)
    events.sort()

    for event in events:
        if event.c1.stuck:
            event.c2.update_position(event.t2)

        else:
            event.c1.update_position(event.t2)
            event.c2.update_position(event.t2)
            if event.t1 < event.t2:
                event.c2.stuck = True
    return cows


def find_next_event(n, e):
    # 0 for intersecting at same time
    # 1 if north passes first
    # -1 if east passes first
    # "Inf" if it does not intersect
    nx = n[0]
    ny = n[1]    # goes up
    ex = e[0]    # goes east
    ey = e[1]
    if nx < ex or ey < ny:
        return "Inf", 1000000001, 1000000001
    intersection_point = (nx, ey)
    n_dist = abs(ny - intersection_point[1])
    e_dist = abs(ex - intersection_point[0])
    if n_dist == e_dist:
        return 0, n_dist, e_dist
    if e_dist > n_dist:
        return 1, n_dist, e_dist
    if n_dist > e_dist:
        return -1, n_dist, e_dist


def solve(N, norths, easts):
    res = ["Infinity" for _ in range(N)]

    # 1 for not stopped; 0 for stopped
    stop_track = [1 for _ in range(N)]

    # stopped = set()
    # north_stopped = []
    # east_stopped = []
    # keep track of the shortest distance that north travels before stopping
    # keep track of the shortest distance that east travels before stopping

    # for n, n_place in norths:
    #     for e, e_place in easts:
    #         event, n_dist, e_dist = find_next_event(n, e)
    #         if event == 1:
    #             east_stopped.append([n_place, e_place, n_dist, e_dist])
    #         elif event == -1:
    #             north_stopped.append([n_place, e_place, n_dist, e_dist])
    # print(north_stopped, east_stopped)
    # north_stopped.sort(key=lambda x: x[2])
    # east_stopped.sort(key=lambda x: x[3])
    # print(north_stopped, east_stopped)

    for n, n_place in norths:
        for e, e_place in easts:
            event, n_dist, e_dist = find_next_event(n, e)
            # if e_place == 2 or n_place == 2:
            #     print(event, n_dist, e_dist, n, e)
            if event == 0 or event == "Inf":
                continue
            if event == 1:
                if res[n_place] != "Infinity" and stop_track[n_place] == 0 and n_dist > res[n_place]:
                    continue
                if stop_track[e_place] == 1:
                    stop_track[e_place] = 0
                    res[e_place] = e_dist
                else:
                    if e_dist < res[e_place]:
                        res[e_place] = e_dist
            if event == -1:
                if res[e_place] != "Infinity" and stop_track[e_place] == 0 and e_dist > res[e_place]:
                    continue
                if stop_track[n_place] == 1:
                    stop_track[n_place] = 0
                    res[n_place] = n_dist
                else:
                    if n_dist < res[n_place]:
                        res[n_place] = n_dist
    return res


def main():
    n = int(input().strip())
    cows_input = []
    for i in range(n):
        d, x, y = input().strip().split()
        cows_input.append((d, int(x), int(y)))
    cows = solve2(n, cows_input)
    for cow in cows:
        print(cow.report_result())


def test():
    for i in range(1, 11):
        with open(f"Stuck_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            cows_input = []
            for _ in range(n):
                d, x, y = fin.readline().strip().split()
                cows_input.append((d, int(x), int(y)))
        cows = solve2(n, cows_input)
        with open(f"test_outs/{i}.out", "w") as fout:
            for cow in cows:
                fout.write(f"{cow.report_result()}\n")


if __name__ == '__main__':
    test()
