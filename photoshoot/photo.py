def solve(N, b):
    for a_0 in range(1, N+1):
        a_list = [a_0]
        a_set = set(a_list)
        done = True
        for j in range(N-1):
            a_j = b[j] - a_list[-1]
            if a_j in a_set:
                done = False
                break
            if a_j > N or a_j < 1:
                done = False
                break
            a_list.append(a_j)
            a_set.add(a_j)
        if done:
            return a_list


def main():
    with open("photo.in", "r") as fin:
        N = int(fin.readline().strip())
        b = []
        for item in fin.readline().strip().split():
            b.append(int(item))

    a_list = solve(N, b)
    with open("photo.out", "w") as fout:
        space = ""
        for cow in a_list:
            fout.write(f"{space}{cow}")
            space = " "
        fout.write("\n")


def test():
    for j in range(1, 11):
        with open(f"photoshoot_test_data/{j}.in", "r") as fin:
            N = int(fin.readline().strip())
            b = []
            for item in fin.readline().strip().split():
                b.append(int(item))

        a_list = solve(N, b)
        with open(f"test_outs/{j}.out", "w") as fout:
            space = ""
            for cow in a_list:
                fout.write(f"{space}{cow}")
                space = " "
            fout.write("\n")


if __name__ == "__main__":
    test()
