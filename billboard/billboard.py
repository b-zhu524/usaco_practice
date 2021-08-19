import sys


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.x2, self.y1, self.y2, = x1, x2, y1, y2
        self.length = self.x2 - self.x1
        self.height = self.y2 - self.y1
        self.area = self.length * self.height

    def intersection(self, other_rect):
        delta_x = max(0, min(self.x2, other_rect.x2) -
                      max(self.x1, other_rect.x1))
        delta_y = max(0, min(self.y2, other_rect.y2) -
                      max(self.y1, other_rect.y1))
        return delta_x * delta_y
    #
    # def union(self, other_rect):
    #     return self.area + other_rect.area - self.intersection(other_rect)


if __name__ == '__main__':
    sys.stdin = open("billboard.in", "r")
    sys.stdout = open("billboard.out", "w")

    x1, y1, x2, y2 = map(int, input().split())
    b1 = Rectangle(x1, y1, x2, y2)

    x1, y1, x2, y2 = map(int, input().split())
    b2 = Rectangle(x1, y1, x2, y2)

    x1, y1, x2, y2 = map(int, input().split())
    truck = Rectangle(x1, y1, x2, y2)

    result = b1.area + b2.area - (truck.intersection(b1) + truck.intersection(b2))

    print(result)
