def years_apart():
    pass


def solve():
    zodiac_idx = {"Ox": 1, "Tiger": 2, "Rabbit": 3, "Dragon": 4, "Snake": 5, "Horse": 6, "Goat": 7, "Monkey": 8,
                  "Rooster": 9, "Dog": 10, "Pig": 11, "Rat": 12}

def main():
    with open(f"zodiac.in", "r") as fin:
        n = int(fin.readline().strip())
        cows = dict()
        for _ in range(n):
            phrase = fin.readline().strip().split()
            name, direction, zodiac, other = phrase[0], phrase[3], phrase[4], phrase[-1]
            cows[name] = (direction, zodiac, other)


if __name__ == '__main__':
    main()
