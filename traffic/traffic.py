def first_none(traffic):
    for i in range(len(traffic)):
        if traffic[i][0] == "none":
            return i


def solve(N, traffic):
    # forward
    start_idx = first_none(traffic)
    low, high = traffic[start_idx][1], traffic[start_idx][2]
    for i in range(start_idx+1, len(traffic)):
        ramp = traffic[i][0]
        if ramp == "none":
            low = max(low, traffic[i][1])
            high = min(high, traffic[i][2])
        elif ramp == "on":
            low += traffic[i][1]
            high += traffic[i][2]
        else:
            low -= traffic[i][2]
            high -= traffic[i][1]

        low = max(low, 0)
        high = min(high, 1000)
    forward_res = (low, high)

    # backward
    for i in range(len(traffic)-1, -1, -1):
        ramp = traffic[i][0]
        if ramp == "none":
            low = max(low, traffic[i][1])
            high = min(high, traffic[i][2])
        elif ramp == "off":
            low += traffic[i][1]
            high += traffic[i][2]
        else:
            low -= traffic[i][2]
            high -= traffic[i][1]
        low = max(low, 0)
        high = min(high, 1000)

    backward_res = (low, high)

    return backward_res, forward_res


def main():
    with open("traffic.in", "r") as fin:
        N = int(fin.readline().strip())
        traffic = []
        for i in range(N):
            status, low, high = fin.readline().strip().split()
            traff_status = (status, int(low), int(high))
            traffic.append(traff_status)

    backward, forward = solve(N, traffic)
    with open("traffic.out", "w") as fout:
        fout.write(f"{backward[0]} {backward[1]}\n")
        fout.write(f"{forward[0]} {forward[1]}\n")


def test():
    for j in range(1, 11):
        with open(f"traffic_test_data/{j}.in", "r") as fin:
            N = int(fin.readline().strip())
            traffic = []
            for i in range(N):
                status, low, high = fin.readline().strip().split()
                traff_status = (status, int(low), int(high))
                traffic.append(traff_status)

        backward, forward = solve(N, traffic)
        with open(f"test_outs/{j}.out", "w") as fout:
            fout.write(f"{backward[0]} {backward[1]}\n")
            fout.write(f"{forward[0]} {forward[1]}\n")


if __name__ == "__main__":
    test()
