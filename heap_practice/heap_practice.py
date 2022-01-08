class MinHeap:
    def __init__(self):
        self.arr = []
        self.n = 0

    def pop(self):
        if len(self.arr) == 0:
            return None
        return self.arr[-1]

    def percolate_down(self, i):
        pass


if __name__ == "__main__":
    pass
