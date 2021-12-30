def solve(time_list, shifts, total_time):
    max_time = 0
    for start_fire, end_fire in shifts:
        new_time = total_time
        for i in range(start_fire, end_fire):
            if time_list[i] - 1 == 0:
                new_time -= 1

        if new_time > max_time:
            max_time = new_time
    return max_time


def main():
    with open("lifeguards.in", "r") as fin:
        n = int(fin.readline().strip())
        shifts = []
        for _ in range(n):
            start, end = fin.readline().strip().split()
            shifts.append((int(start), int(end)))

        time_list = [0] * 1000
        total_time = 0
        for s, e in shifts:
            for i in range(s, e):
                if time_list[i] == 0:
                    total_time += 1
                time_list[i] += 1

    with open("lifeguards.out", "w") as fout:
        fout.write(f"{solve(time_list, shifts, total_time)}\n")


def test():
    for j in range(1, 11):
        with open(f"lifeguards_test_data/{j}.in", "r") as fin:
            n = int(fin.readline().strip())
            shifts = []
            for _ in range(n):
                start, end = fin.readline().strip().split()
                shifts.append((int(start), int(end)))

            time_list = [0] * 1000
            total_time = 0
            for s, e in shifts:
                for i in range(s, e):
                    if time_list[i] == 0:
                        total_time += 1
                    time_list[i] += 1

        with open(f"test_outs/{j}.out", "w") as fout:
            fout.write(f"{solve(time_list, shifts, total_time)}\n")


if __name__ == '__main__':
    test()
