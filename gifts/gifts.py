def cost_with_coupon(wish):
    p, s = wish
    return (p/2) + s


def solve(B, N, wishes):
    wishes.sort(key=lambda x: x[0] + x[1])
    budget = B
    largest_price_include = 0

    for i in range(len(wishes)):
        p, s = wishes[i]
        if budget < p + s:
            break

        if wishes[i][0] > largest_price_include:
            largest_price_include = wishes[i][0]

        budget -= p + s
    happy_cows = i

    # apply coupon to opt 1
    opt1_happy_cows = happy_cows
    opt1_budget = budget + (largest_price_include / 2)
    for i in range(happy_cows, N):
        if budget <= 0:
            break

        cost = sum(wishes[i])
        if opt1_budget >= cost:
            return opt1_happy_cows + 1

    # apply coupon to opt2
    opt2_happy_cows = happy_cows
    opt2_budget = budget
    for i in range(happy_cows, N):
        cost = cost_with_coupon(wishes[i])
        if cost <= opt2_budget:
            opt2_happy_cows += 1
            return opt2_happy_cows

    return max(opt1_happy_cows, opt2_happy_cows)


def main():
    with open("gifts.in", "r") as fin:
        N, B = fin.readline().strip().split()
        N, B = int(N), int(B)
        wishes = []
        for _ in range(N):
            p, s = fin.readline().strip().split()
            p, s = int(p), int(s)
            wishes.append((p, s))

    with open("gifts.out", "w") as fout:
        out = str(solve(B, N, wishes))
        fout.write(out)


if __name__ == "__main__":
    main()
