from functools import cmp_to_key


def solve(photos):
    # nested function
    def cmp_cow_ids(c1, c2):
        less_than_votes = 0
        for photo in photos:
            if photo[c1] < photo[c2]:
                less_than_votes += 1
        if less_than_votes >= 3:
            return -1
        else:
            return 1

    # actual code
    # create list of cow_ids to be sorted
    cow_ids = []
    for cow_id in photos[0]:
        cow_ids.append(cow_id)
    cow_ids.sort(key=cmp_to_key(cmp_cow_ids))
    return cow_ids


def main():
    with open("photo.in", "r") as fin:
        N = int(fin.readline().strip())
        photos = []
        for i in range(5):
            photo = {}
            for j in range(N):
                current_id = int(fin.readline().strip())
                photo[current_id] = j
            photos.append(photo)
    with open("photo.out", "w") as fout:
        out = solve(photos)
        for cow_id in out:
            fout.write(f"{cow_id}\n")


def test():
    for k in range(1, 11):
        with open(f"cow_photo_test_data/I.{k}", "r") as fin:
            N = int(fin.readline().strip())
            photos = []
            for i in range(5):
                photo = {}
                for j in range(N):
                    current_id = int(fin.readline().strip())
                    photo[current_id] = j
                photos.append(photo)
        with open(f"test_outs/O.{k}", "w") as fout:
            out = solve(photos)
            for cow_id in out:
                fout.write(f"{cow_id}\n")


if __name__ == "__main__":
    test()
