def solve(N, cows):
	cows.sort(key=lambda x: x[0])

	min_safe_radius = cows[-1][0] - cows[0][0]
	for i in range(N-1):
		if cows[i+1][1] != cows[i][1]:
			min_safe_radius = min(min_safe_radius, cows[i+1][0] - cows[i][0])

	i = 0
	count = 0
	while i < N:
		if cows[i][1] == 1:
			i += 1
			count += 1
			while i < N and cows[i][1] != 0 and cows[i][0] - cows[i-1][0] < min_safe_radius:
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


def test():
	for j in range(1, 11):
		with open(f"socdist2_test_data/{j}.in", "r") as fin:
			N = int(fin.readline().strip())
			cows = []
			for i in range(N):
				cows.append([int(x) for x in fin.readline().strip().split()])
		with open(f"test_outs/{j}.out", "w") as fout:
			out = solve(N, cows)
			fout.write(f"{out}\n")


if __name__ == "__main__":
	test()
