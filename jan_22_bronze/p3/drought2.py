def solve(n, cows):
    pass


def main():
    t = int(input())
    cases = []
    for _ in range(t):
        n = int(input())
        temp = input().strip().split()
        cows = [int(x) for x in temp]
        cases.append([n, cows])
    for i in range(t):
        curr_n, curr_cows = cases[i]
        print(f"{solve(curr_n, curr_cows)}")


if __name__ == '__main__':
    main()
