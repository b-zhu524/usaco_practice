def longest_common_substring(s1, s2):
    # generate all substrings s1
    s1_substrings = [""]
    for start1 in range(len(s1)):
        for end1 in range(start1, len(s1)):
            s1_substrings.append(s1[start1:end1+1])

    # generate all substrings s2
    s2_substrings = [""]
    for start2 in range(len(s2)):
        for end2 in range(start2, len(s2)):
            s2_substrings.append(s2[start2:end2+1])

    print(len(s1_substrings), len(s2_substrings))
    # compare
    common_substring_longest = ("", 0)
    for i in range(len(s1_substrings)):
        for j in range(len(s2_substrings)):
            s1_len = len(s1_substrings[i])
            if s1_substrings[i] == s2_substrings[j] and s1_len > common_substring_longest[1]:
                common_substring_longest = (s1_substrings[i], s1_len)
    return common_substring_longest[0]


def count_digits(num):
    digit_count = 0
    while num != 0:
        digit_count += 1
        num //= 10
    return digit_count


if __name__ == "__main__":
    print(longest_common_substring("12346754e7081234567890ty63w25478u97y789023456drcvg6s8 706fdf56e56guigetyhuji\n"
                                   "j6578u9i1234567890582461",
                                   "2384157453 yu6 576485545812345678908455418544856448845frvcg ttyrf65e3ws576 \n"
                                   "8168547890234566yhu4"))
