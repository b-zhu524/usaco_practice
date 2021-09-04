# def min_distance(stalls):
#     i = 0
#     min_dist = None
#     while i < len(stalls) and stalls[i] != 1:
#         i += 1
#     while True:
#         j = i + 1
#         while j < len(stalls) and stalls[j] != 1:
#             j += 1
#         if j == len(stalls):
#             break
#         dist = j - i
#         if min_dist is None or dist < min_dist:
#             min_dist = dist
#
#         i = j
#     return min_dist
#
#
# def largest_gap(stalls):
#     # find the gap between 1's
#     i = 0
#     max_gap = None
#     start, end = -1, -1
#
#     while i < len(stalls) and stalls[i] != 1:
#         i += 1
#
#     while True:
#         j = i + 1
#         while j < len(stalls) and stalls[j] != 1:
#             j += 1
#         if j >= len(stalls):
#             break
#         gap = j - i
#         if max_gap is None or max_gap < gap:
#             start, end = i, j
#             max_gap = gap
#         i = j
#     return start, end


def make_dist_list(stalls):
    dist_list = []
    for i in range(len(stalls)):
        if stalls[i] == 1:
            dist_list.append(i)
    return dist_list


def largest_gap(stalls):
    max_dist = -1
    dist_list = make_dist_list(stalls)
    start, end = -1, -1

    for i in range(1, len(dist_list)):
        if dist_list[i] - dist_list[i-1] > max_dist:
            start, end = dist_list[i-1], dist_list[i]
            max_dist = dist_list[i] - dist_list[i-1]
    return start, end


def min_distance(stalls):
    dist_list = make_dist_list(stalls)
    min_dist = None
    for i in range(1, len(dist_list)):
        if min_dist is None or dist_list[i] - dist_list[i-1] < min_dist:
            min_dist = dist_list[i] - dist_list[i-1]
    return min_dist


def solve(N, stalls):
    best_result = -1

    # opt 1: add corners
    temp_stalls = stalls.copy()
    if temp_stalls[0] == 0 and temp_stalls[-1] == 0:
        temp_stalls[0], temp_stalls[-1] = 1, 1
        dist = min_distance(temp_stalls)
        best_result = max(best_result, dist)

    # opt 2a: one in left corner, one in gap
    temp_stalls = stalls.copy()
    if temp_stalls[0] == 0:
        temp_stalls[0] = 1
        start, end = largest_gap(temp_stalls)
        if start != -1 and end - start > 1:
            temp_stalls[(start + end) // 2] = 1
            dist = min_distance(temp_stalls)
            best_result = max(best_result, dist)

    # opt 2b: one in right corner, one in gap
    temp_stalls = stalls.copy()
    if temp_stalls[-1] == 0:
        temp_stalls[-1] = 1
        start, end = largest_gap(temp_stalls)
        if start != -1 and end - start > 1:
            temp_stalls[(start + end) // 2] = 1
            dist = min_distance(temp_stalls)
            best_result = max(best_result, dist)

    # opt 3: both in same gap
    temp_stalls = stalls.copy()
    start, end = largest_gap(temp_stalls)
    if start != -1 and end - start > 2:
        temp_stalls[(start + end) // 3] = 1
        temp_stalls[(((start + end)*2) // 3)] = 1
        dist = min_distance(temp_stalls)
        best_result = max(best_result, dist)

    # opt 4: 1 in each gap
    temp_stalls = stalls.copy()
    start, end = largest_gap(temp_stalls)
    if start != -1 and end - start > 1:
        temp_stalls[(start + end) // 2] = 1
    start, end = largest_gap(temp_stalls)
    if start != -1 and end - start > 1:
        temp_stalls[(start + end) // 2] = 1
        dist = min_distance(temp_stalls)
        best_result = max(best_result, dist)

    return best_result


def main():
    with open("socdist1.in", "r") as fin:
        N = int(fin.readline().strip())
        current_cows_str = fin.readline().strip()
        current_cows = [int(num) for num in current_cows_str]

    with open("socdist1.out", "w") as fout:
        if len(current_cows) == 0:
            fout.write(str(N-1))
            return

        out = solve(N, current_cows)
        fout.write(f"{out}\n")


def test():
    for i in range(1, 16):
        with open(f"socdist1_test_data/{i}.in", "r") as fin:
            N = int(fin.readline().strip())
            current_cows_str = fin.readline().strip()
            current_cows = [int(num) for num in current_cows_str]

        with open(f"test_outs/{i}.out", "w") as fout:
            if len(current_cows) == 0:
                fout.write(str(N - 1))
                return

            out = solve(N, current_cows)
            fout.write(f"{out}\n")


if __name__ == "__main__":
    test()
