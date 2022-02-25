import logging
logging.basicConfig(filename="example.log", encoding="utf-8", level=logging.DEBUG)


def double_arr(a):
    for i in range(len(a)):
        logging.warning(f"before the first loop i={i}, a={a}")
        a[i] += 2
        logging.warning(f"after the first loop i={i}, a={a}")


if __name__ == '__main__':
    a = [1, 2, 3]
    double_arr(a)
    print(a)
