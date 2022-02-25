def is_highest(curr_highest, cow_status_dict, cow_name):
    if cow_status_dict[cow_name] > curr_highest[1]:
        return 2
    elif cow_status_dict[cow_name] == curr_highest[1]:
        return 1
    return False



def solve(n, cows, cow_status_dict):
    cows.sort(key=lambda x: x[0])

    changes = 0
    curr_highest = [set(), None]
    for cow in cows:
        curr_highest[0].add(cow[1])
    curr_highest[-1] = cow_status_dict[cow[1]]


    # make changes
    for _, cow_name, m_change in cows:
        cow_status_dict[cow_name] += m_change

        cow_rank = is_highest(curr_highest, cow_status_dict, cow_name)
        if cow_rank:
            if cow_rank == 2:
                curr_highest = [set()]
                curr_highest[0].add(cow_name)
                curr_highest.append(cow_status_dict[cow_name])
            elif cow_rank == 1:
                curr_highest.add(cow_name)
            changes += 1
        else:
            if cow in curr_highest:
                curr_highest[0].remove(cow)
                changes += 1
    return changes


def main():
    with open("measurement.in", "r") as fin:
        n = int(fin.readline().strip())
        cows = []
        cow_status_dict = dict()
        for _ in range(n):
            date, cow, m_change = fin.readline().strip().split()
            if m_change[0] == "+":
                m_change = m_change[1]

            date, m_change = int(date), int(m_change)
            cows.append([date, cow, m_change])

            if cow not in cow_status_dict:
                cow_status_dict[cow] = 7

    res = solve(n, cows, cow_status_dict)
    with open("measurement.out", "w") as fout:
        fout.write(f"{res}\n")

if __name__ == "__main__":
    main()
