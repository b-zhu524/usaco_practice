class Cow:
    photos = None

    def __init__(self, cow_id):
        self.cow_id = cow_id

    def __lt__(self, other):
        greater_than_count = 0
        less_than_count = 0
        for photo in Cow.photos:
            if photo[self.cow_id] < photo[other.cow_id]:
                less_than_count += 1
            else:
                greater_than_count += 1
        return less_than_count > greater_than_count


def solve(photos):
    Cow.photos = photos
    cow_ids = []
    for cow_id in photos[0]:
        cow_ids.append(Cow(cow_id))
    cow_ids.sort()
    return cow_ids


def main():
    photos = []
    with open("photo.in", "r") as fin:
        N = int(fin.readline().strip())
        for i in range(5):
            photo = {}
            for j in range(N):
                current_id = fin.readline().strip()
                photo[current_id] = j
            photos.append(photo)
    with open("photo.out", "w") as fout:
        for result in solve(photos):
            fout.write(f"{result.cow_id}\n")


if __name__ == "__main__":
    main()
