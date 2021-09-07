def solve(N, cows):
	cows.sort(key=lambda x: x[0])
	min_radius = cows[-1][0] - cows[0][0]

	for i in range(N-1):
		if cows[i][1] != cows[i+1][1]:
			min_radius = min(min_radius, cows[i+1][0]-cows[i][0])

	i = 0
	count = 0
	while i < N:
		if cows[i][1] == 1:
			count += 1
			i += 1
			while i < N and cows[i][1] == 1 and cows[i][0] - cows[i-1][0] < min_radius:
				i += 1
		else:
			i += 1
	return count


def main():
	with open("socdist2.in", "r") as fin:
		N = int(fin.readline().strip())
		cows = []
		for i in range(N):
			cows.append([int(x) for x in fin.readline().strip().split()])
	with open("socdist2.out", "w") as fout:
		out = solve(N, cows)
		fout.write(f"{out}\n")


if __name__ == "__main__":
	main()
