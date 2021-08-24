def search(t, arr):
    for i in range(len(arr)):
        if arr[i] == t:
            return i
    return -1


def solve(flowers, N):
    count = 0
    for i in range(N):
        accumulate = 0
        seen = set()
        for j in range(i, N):
            accumulate += flowers[j]
            a = accumulate / (j - i + 1)
            seen.add(flowers[j])
            if a in seen:
                count += 1
    return count


if __name__ == '__main__':
    N = int(input())
    flowers = [int(x) for x in input().split()]
    solution = solve(flowers, N)
    print(solution)
