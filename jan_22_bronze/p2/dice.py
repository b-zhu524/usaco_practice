def beat(a, b):
    a_vict = 0
    b_vict = 0
    tie = 0
    for num1 in a:
        for num2 in b:
            if num1 > num2:
                a_vict += 1
            elif num1 == num2:
                tie += 1
            else:
                b_vict += 1
    if a_vict > b_vict:
        return 1
    if a_vict == b_vict:
        return 0
    return -1


def solve(a, b):
    a_beat_b = beat(a, b)
    # a beat b
    if a_beat_b == 1:
        for n1 in range(1, 11):
            for n2 in range(1, 11):
                for n3 in range(1, 11):
                    for n4 in range(1, 11):
                        c = [n1, n2, n3, n4]
                        if beat(c, a) == 1 and beat(b, c) == 1:
                            return True
        return False

    elif a_beat_b == -1:
        for n1 in range(1, 11):
            for n2 in range(1, 11):
                for n3 in range(1, 11):
                    for n4 in range(1, 11):
                        c = [n1, n2, n3, n4]
                        if beat(c, b) == 1 and beat(a, c) == 1:
                            return True
        return False


def main():
    t = int(input())
    a = []
    b = []
    for _ in range(t):
        curr_a = []
        curr_b = []
        die = input().split()
        for i in range(4):
            curr_a.append(int(die[i]))
        for i in range(4, 8):
            curr_b.append(int(die[i]))
        a.append(curr_a)
        b.append(curr_b)

    for i in range(t):
        res = solve(a[i], b[i])
        if res:
            print("yes")
        else:
            print("no")


if __name__ == '__main__':
    main()
