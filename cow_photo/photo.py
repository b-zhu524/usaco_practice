# def find_cow_idx(cow_id, photo):
#     for i in range(len(photo)):
#         if photo[i] == cow_id:
#             return i
#     return -1


class Cow:
    photos = None

    def __init__(self, cow_id):
        self.cow_id = cow_id

    def __lt__(self, other):
        vote = 0
        for photo in Cow.photos:
            idx_1 = photo[self.cow_id]
            idx_2 = photo[other.cow_id]
            if idx_1 < idx_2:
                vote += 1
        return vote >= 3


def solve(N, photos):
    Cow.photos = photos
    cows = []
    for cow_id in photos[0]:
        cows.append(Cow(cow_id))
    cows.sort()
    return cows


def main():
    photos = []
    with open("photo.in", "r") as fin:
        N = int(fin.readline().strip())
        for i in range(5):
            photo = {}
            for j in range(N):
                cow_id = int(fin.readline().strip())
                photo[cow_id] = j
            photos.append(photo)

    with open("photo.out", "w") as fout:
        for cow in solve(N, photos):
            fout.write(f"{cow.cow_id}\n")


def test():
    for k in range(1, 11):
        photos = []
        with open(f"cow_photo_test_data/I.{k}", "r") as fin:
            N = int(fin.readline().strip())
            for i in range(5):
                photo = {}
                for j in range(N):
                    cow_id = int(fin.readline().strip())
                    photo[cow_id] = j
                photos.append(photo)

        with open(f"test_outs/O.{k}", "w") as fout:
            for cow in solve(N, photos):
                fout.write(f"{cow.cow_id}\n")


if __name__ == "__main__":
    test()
