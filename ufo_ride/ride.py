def solve(com_name, group_name):
    alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                  'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                  'V', 'W', 'X', 'Y', 'Z']
    num_list = list(range(1, 27))

    alpha_dict = dict(zip(alpha_list, num_list))

    com_val = 1
    for char in com_name:
        com_val *= alpha_dict[char]

    group_val = 1
    for char in group_name:
        group_val *= alpha_dict[char]

    if com_val % 47 == group_val % 47:
        return "GO"
    return "STAY"


def main():
    with open("ride.in", "r") as fin:
        com_name = fin.readline().strip()
        group_name = fin.readline().strip()

    res = solve(com_name, group_name)
    with open("ride.out", "w") as fout:
        fout.write(f"{res}\n")


if __name__ == '__main__':
    main()
