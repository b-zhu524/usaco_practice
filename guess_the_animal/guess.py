def solve(animals, description_count):
    print(description_count)
    max_count = 0
    for animal in animals:
        descriptions = animals[animal]
        shared_feature_cnt = 0
        for description in descriptions:
            if description_count[description] > 1:
                print(animal, description)
                shared_feature_cnt += 1
        print(max_count, shared_feature_cnt, animal)
        max_count = max(max_count, shared_feature_cnt)
    return max_count + 1


def main():
    with open("guess.in", "r") as fin:
        n = int(fin.readline().strip())
        description_count = dict()
        animals = dict()

        for _ in range(n):
            animal, cnt, *descriptions = fin.readline().strip().split()

            for description in descriptions:
                if description not in description_count:
                    description_count[description] = 1
                else:
                    description_count[description] += 1

            animals[animal] = descriptions

    res = solve(animals, description_count)
    with open("guess.out", "w") as fout:
        fout.write(f"{res}\n")


def test():
    for i in range(1, 11):
        with open(f"guess_test_data/{i}.in", "r") as fin:
            n = int(fin.readline().strip())
            description_count = dict()
            animals = dict()

            for _ in range(n):
                animal, cnt, *descriptions = fin.readline().strip().split()

                for description in descriptions:
                    if description not in description_count:
                        description_count[description] = 1
                    else:
                        description_count[description] += 1

                animals[animal] = descriptions

        res = solve(animals, description_count)
        with open(f"test_outs/{i}.out", "w") as fout:
            fout.write(f"{res}\n")


if __name__ == '__main__':
    main()
