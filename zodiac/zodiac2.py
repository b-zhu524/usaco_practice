def count_years(start_zodiac, end_zodiac, direction, zodiacs, zodiac_indices):
    if direction == "previous":
        idx = (zodiac_indices[start_zodiac] - 1) % 12
        distance = -1
    else:
        idx = (zodiac_indices[start_zodiac] + 1) % 12
        distance = 1

    while zodiacs[idx] != end_zodiac:
        if direction == "previous":
            distance -= 1
            idx = (idx - 1) % 12
        else:
            distance += 1
            idx = (idx + 1) % 12
    return distance


def solve(phrases):
    zodiac_indices = {"Ox": 0, "Tiger": 1, "Rabbit": 2, "Dragon": 3,
                      "Snake": 4, "Horse": 5, "Goat": 6, "Monkey": 7,
                      "Rooster": 8, "Dog": 9, "Pig": 10, "Rat": 11}

    zodiacs = ["Ox", "Tiger", "Rabbit", "Dragon",
               "Snake", "Horse", "Goat", "Monkey",
               "Rooster", "Dog", "Pig", "Rat"]

    years_from_bessie = {"Bessie": 0}
    cow_zodiac = {"Bessie": "Ox"}

    for phrase in phrases:
        name = phrase[0]
        direction = phrase[3]
        zodiac = phrase[4]
        compare_name = phrase[7]

        cow_zodiac[name] = zodiac
        compare_years = count_years(cow_zodiac[compare_name], zodiac,
                                    direction, zodiacs, zodiac_indices)
        years_from_bessie[name] = compare_years + years_from_bessie[compare_name]

        if "Elsie" in cow_zodiac:
            return abs(years_from_bessie["Elsie"])
    return -1


def main():
    N = int(input())
    phrases = []
    for i in range(N):
        phrases.append(input().strip().split())
    print(f"{solve(phrases)}\n")


def test():
    for j in range(1, 11):
        with open(f"Zodiac_Test_Data/{j}.in", "r") as fin:
            N = int(fin.readline().strip())
            phrases = []
            for i in range(N):
                phrases.append(fin.readline().strip().split())
        with open(f"test_outs/{j}.out", "w") as fout:
            fout.write(f"{solve(phrases)}\n")


if __name__ == "__main__":
    test()
