def min_distance(stalls):
    i = 0
    min_dist = None
    while i < len(stalls) and stalls[i] != 1:
        i += 1
    while True:
        j = i + 1
        while j < len(stalls) and stalls[j] != 1:
            j += 1
        if j == len(stalls):
            break
        dist = j - i
        if min_dist is None or dist < min_dist:
            min_dist = dist

        i = j
    return min_dist


def largest_gap(stalls):
    i = 0

    while i < len(stalls) and stalls[i] != 1:
        i += 1
    max_gap = i + 1
    start, end = 0, i

    while True:
        j = i + 1
        while j < len(stalls) and stalls[j] != 1:
            j += 1
        if j == len(stalls):
            if stalls[-1] == 0:
                gap = j - i
                if max_gap < gap:
                    start, end = i, j-1
                    max_gap = gap
            break
        gap = j - i
        if max_gap < gap:
            start, end = i, j
            max_gap = gap
        i = j
    return start, end


def test():
    stalls = [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0]
    out = largest_gap(stalls)
    print(out)


if __name__ == "__main__":
    l = [1, 2, 3]
    temp_l = l[:]
    temp_l[1] = 10
    print(l)


# def make_dist_list(stalls):
#     dist_list = []
#     for i in range(len(stalls)):
#         if stalls[i] == 1:
#             dist_list.append(i)
#     return dist_list
#
#
# def largest_gap(stalls):
#     max_dist = -1
#     dist_list = make_dist_list(stalls)
#     start, end = -1, -1
#
#     for i in range(1, len(dist_list)):
#         if dist_list[i] - dist_list[i-1] > max_dist:
#             start, end = dist_list[i-1], dist_list[i]
#             max_dist = dist_list[i] - dist_list[i-1]
#     return start, end
#
#
# def min_distance(stalls):
#     dist_list = make_dist_list(stalls)
#     min_dist = None
#     for i in range(1, len(dist_list)):
#         if min_dist is None or dist_list[i] - dist_list[i-1] < min_dist:
#             min_dist = dist_list[i] - dist_list[i-1]
#     return min_dist




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
