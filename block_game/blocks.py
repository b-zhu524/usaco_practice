def count_letters(word):
	alpha_counter = [0] * 26
	for letter in word:
		idx = ord(letter) - ord("a")
		alpha_counter[idx] += 1
	return alpha_counter


def solve(boards):
	alpha_counter = [0] * 26
	for word1, word2 in boards:
		counter1 = count_letters(word1)
		counter2 = count_letters(word2)
		for idx in range(26):
			alpha_counter[idx] += max(counter1[idx], counter2[idx])
	return alpha_counter


def count_letters_dict(word):
	alpha_dict = {}
	for letter in word:
		key = ord(letter) - ord("a")
		if key in alpha_dict:
			alpha_dict[key] += 1
		else:
			alpha_dict[key] = 1
	return alpha_dict


def get_max_count(dict1, dict2, key):
	count = 0
	if key in dict1:
		count = max(count, dict1[key])
	if key in dict2:
		count = max(count, dict2[key])
	return count


def solve_dict(boards):
	alpha_counter = [0] * 26
	for word1, word2 in boards:
		counter1 = count_letters_dict(word1)
		counter2 = count_letters_dict(word2)
		for i in range(26):
			alpha_counter[i] += get_max_count(counter1, counter2, i)
	return alpha_counter


def main():
	with open("blocks.in", "r") as fin:
		N = int(fin.readline().strip())
		boards = []
		for _ in range(N):
			word1, word2 = fin.readline().strip().split()
			boards.append((word1, word2))
	with open("blocks.out", "w") as fout:
		out = solve(boards)
		for count in out:
			fout.write(f"{count}\n")


def test():
	for i in range(1, 11):
		with open(f"block_game_test_data/{i}.in", "r") as fin:
			N = int(fin.readline().strip())
			boards = []
			for _ in range(N):
				word1, word2 = fin.readline().strip().split()
				boards.append((word1, word2))
		with open(f"test_outs/{i}.out", "w") as fout:
			out = solve(boards)
			for count in out:
				fout.write(f"{count}\n")


if __name__ == "__main__":
	test()
