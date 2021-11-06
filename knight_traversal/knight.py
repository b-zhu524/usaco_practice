def permutation(L, result, selected, depth):
	print(result, selected, depth)
	if depth == len(L):
		print(result)
		return

	for i in range(len(L)):
		print(i)
		if selected[i]:
			continue

		result.append(L[i])
		selected[i] = True
		permutation(L, result, selected, depth+1)

		result.pop()
		selected[i] = False

		print(result, selected, depth)


def solve(board):
	chessboard = [[-1 for _ in range(n)] for _ in range(n)]

	if -1 not in chessboard:
		return chessboard


def main():
	permutation(['a', 'b', ' c'], [], [False, False, False], 0)


if __name__ == "__main__":
	main()
