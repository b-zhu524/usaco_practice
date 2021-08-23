import sys

if __name__ == '__main__':
    sys.stdin = open("shell.in", "r")
    sys.stdout = open("shell.out", "w")
    N = map(int, input().split())

