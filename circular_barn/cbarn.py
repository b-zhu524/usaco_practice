def solve(n, rooms):
    col_dist = None
    total_cows = sum(rooms)
    for start_room in range(len(rooms)):
        cows = total_cows
        new_col_dist = 0
        room = start_room

        for _ in range(n-1):
            cows -= rooms[room]
            room = (room + 1) % n
            new_col_dist += cows
        if col_dist is None or new_col_dist < col_dist:
            col_dist = new_col_dist
    return col_dist


def main():
    with open("cbarn.in", "r") as fin:
        n = int(fin.readline().strip())
        rooms = []
        for _ in range(n):
            barn = int(fin.readline().strip())
            rooms.append(barn)

    res = solve(n, rooms)
    with open("cbarn.out", "w") as fout:
        fout.write(f"{res}\n")


def test():
    for i in range(1, 11):
        with open(f"cbarn_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            rooms = []
            for _ in range(n):
                barn = int(fin.readline().strip())
                rooms.append(barn)

        res = solve(n, rooms)
        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{res}\n")


if __name__ == "__main__":
    test()
