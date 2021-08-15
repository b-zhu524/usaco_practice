def find_union(a, b, c, d):
    startpoint = max(a, c)
    endpoint = min(b, d)
    intersection_ = endpoint - startpoint
    intersection = max(0, intersection_)
    union = (b - a) + (d - c) - intersection

    return union
