from functools import total_ordering


@total_ordering
class Index:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x=%d, y=%d" % (self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Index):
            return False
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return 1

    def __cmp__(self, other):
        return 1

