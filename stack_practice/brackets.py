from collections import deque


def compatible_bracket(bracket):
    bracket_dict = {")": "(",
                    "]": "[",
                    "}": "{"}
    return bracket_dict[bracket]


def is_compatible(bracket_str):
    bracket_stack = deque()
    for char in bracket_str:
        if char == ")" or char == "}" or char == "]":
            if bracket_stack.pop == char:
                bracket_stack.pop()
                continue
            return False
        elif char == "(" or char == "{" or char == "[":
            bracket_stack.append(char)
    if len(bracket_stack) != 0:
        return False
    return True


if __name__ == "__main__":
    print(is_compatible("[]"))
