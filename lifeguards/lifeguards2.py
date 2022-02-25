def time_covered(events, fire_start, fire_end):
    result = 0
    cnt = 0
    start_time = None
    for event in events:
        if event[0] == fire_start or event[0] == fire_end:
            continue

        if event[1] == "s":
            cnt += 1
            if start_time is None:
                start_time = event[0]
        else:
            cnt -= 1
            if cnt == 0:
                result += event[0] - start_time
                start_time = None
    return result


def solve(events, fire_list):
    max_time_covered = 0
    events.sort(key=lambda x: x[0])
    for start, end in fire_list:
        record_time = time_covered(events, start, end)
        max_time_covered = max(max_time_covered, record_time)
    return max_time_covered


def main():
    with open("lifeguards.in", "r") as fin:
        n = int(fin.readline().strip())
        fire_list = []
        events = []
        for _ in range(n):
            s_event, e_event = fin.readline().strip().split()
            events.append((int(s_event), "s"))
            events.append((int(e_event), "e"))
            fire_list.append((int(s_event), int(e_event)))

    with open("lifeguards.out", "w") as fout:
        fout.write(f"{solve(events, fire_list)}")


def test():
    for i in range(1, 11):
        with open(f"lifeguards_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            fire_list = []
            events = []
            for _ in range(n):
                s_event, e_event = fin.readline().strip().split()
                events.append((int(s_event), "s"))
                events.append((int(e_event), "e"))
                fire_list.append((int(s_event), int(e_event)))

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(events, fire_list)}\n")


if __name__ == '__main__':
    test()
