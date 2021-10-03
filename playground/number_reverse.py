def is_palindrome(num):
    num = str(abs(num))
    reversed_num = num[::-1]
    if num == reversed_num:
        return True
    return False


def is_palindrome2(num):
    num = abs(num)
    original_num = num
    new_num = 0
    while num:
        remainder = num % 10
        new_num = new_num * 10 + remainder
        num //= 10
    return new_num == original_num


if __name__ == '__main__':
    print(is_palindrome2(-1111112111111))
