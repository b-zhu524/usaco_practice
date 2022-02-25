def solve(n, k, events):
    pass


def main():
    with open("stacking.in", "r") as fin:
        n, k = fin.readline().strip().split()
        n, k = int(n), int(k)
        events = []
        for _ in range(k):
            e1, e2 = fin.readline().strip().split()
            events.append((int(e1), "s"))
            events.append((int(e2), "e"))

        events.sort(key=lambda x: x[0])


if __name__ == '__main__':
    main()
