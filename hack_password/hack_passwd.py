import hashlib


def is_password(password):
    hashed = "26c39fed7dd4aa0642e869955fac6aaebb94bee5d18f412128570df591dab504"
    return hashlib.sha256("".join(password).encode("utf-8")).hexdigest() == hashed


def hack():
    password = []
    step = 0
    if search(password, step):
        print("".join(password))
    else:
        print("No solution")


def search(password, step):
    # TODO: implement base
    if step > 6:
        return False

    if step >= 4 and is_password(password):
        print(password)
        return True

    for c in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        password.append(c)
        # TODO: implement recursion
        if search(password, step+1):
            return True

        # Undo
        password.pop()
    return False


if __name__ == "__main__":
    hack()
