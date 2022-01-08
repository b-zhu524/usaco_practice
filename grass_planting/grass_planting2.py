def main():
    with open("planting.in", "r") as fin:
        n = int(fin.readline().strip())
        colors = dict()
        max_colors = 0

        for _ in range(n-1):
            f1, f2 = fin.readline().strip().split()
            f1, f2 = int(f1), int(f2)
            if f1 not in colors:
                colors[f1] = 1
            else:
                colors[f1] += 1

            if f2 not in colors:
                colors[f2] = 1
            else:
                colors[f2] += 1

            if colors[f1] > max_colors:
                max_colors = colors[f1]
            if colors[f2] > max_colors:
                max_colors = colors[f2]

    with open("planting.out", "w") as fout:
        fout.write(f"{max_colors}\n")


def test():
    for i in range(1, 11):
        with open(f"grass_planting_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            colors = dict()
            max_colors = 0

            for _ in range(n - 1):
                f1, f2 = fin.readline().strip().split()
                f1, f2 = int(f1), int(f2)
                if f1 not in colors:
                    colors[f1] = 1
                else:
                    colors[f1] += 1

                if f2 not in colors:
                    colors[f2] = 1
                else:
                    colors[f2] += 1

                if colors[f1] > max_colors:
                    max_colors = colors[f1]
                if colors[f2] > max_colors:
                    max_colors = colors[f2]

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{max_colors+1}\n")


if __name__ == '__main__':
    test()
