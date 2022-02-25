def count_years(own_zodiac, other_zodiac, direction, zodiac_idx, zodiacs):
    if direction == "previous":
        idx = (zodiac_idx[own_zodiac] + 1) % 12
        dist = 1
    else:
        idx = (zodiac_idx[own_zodiac] - 1) % 12
        dist = -1
    while zodiacs[idx] != other_zodiac:
        if direction == "previous":
            dist += 1
            idx = (idx + 1) % 12
        else:
            dist -= 1
            idx = (idx - 1) % 12
    return dist


def solve(n, cows):
    zodiac_idx = {"Ox": 0, "Tiger": 1, "Rabbit": 2, "Dragon": 3, "Snake": 4, "Horse": 5, "Goat": 6, "Monkey": 7,
                  "Rooster": 8, "Dog": 9, "Pig": 10, "Rat": 11}
    zodiacs = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]

    years_from_bessie = {"Bessie": 0}
    zodiac_track = {"Bessie": "Ox"}
    for name, direction, zodiac, other in cows:
        comp_years = count_years(zodiac, zodiac_track[other], direction, zodiac_idx, zodiacs)
        zodiac_track[name] = zodiac
        years_from_bessie[name] = years_from_bessie[other] + comp_years
        if "Elsie" in years_from_bessie:
            return abs(years_from_bessie["Elsie"])
    return -1


def main():
    with open(f"zodiac.in", "r") as fin:
        n = int(fin.readline().strip())
        cows = []
        for _ in range(n):
            phrase = fin.readline().strip().split()
            name, direction, zodiac, other = phrase[0], phrase[3], phrase[4], phrase[-1]
            cows.append((name, direction, zodiac, other))

    with open(f"zodiac.out", "w") as fout:
        fout.write(f"{solve(n, cows)}\n")


def test():
    for i in range(1, 11):
        with open(f"Zodiac_Test_Data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            cows = []
            for _ in range(n):
                phrase = fin.readline().strip().split()
                name, direction, zodiac, other = phrase[0], phrase[3], phrase[4], phrase[-1]
                cows.append((name, direction, zodiac, other))

        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{solve(n, cows)}\n")


if __name__ == '__main__':
    test()
