import sys


def find_union(a, b, c, d):
    startpoint = max(a, c)
    endpoint = min(b, d)
    intersection = max(0, endpoint - startpoint)
    union = (b - a) + (d - c) - intersection
    return union


if __name__ == '__main__':
    sys.stdin = open("paint.in", "r")
    sys.stdout = open("paint.out", "w")

    a, b = map(int, input().split())
    c, d = map(int, input().split())

    print(find_union(a, b, c, d))

