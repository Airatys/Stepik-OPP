class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        print('Вызов метода __eq__()')
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


p = Point(2, 2)
points = [Point(1, 1), Point(2, 2), Point(3, 3)]

print(p in points)