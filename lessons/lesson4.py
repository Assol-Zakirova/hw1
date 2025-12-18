class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # +
    def __add__(v2, v1):
        print(v2.x + v1.x)
    # <
    def __lt__(self, other):
        print(self.x)
        print(other.x)

    # >
    # def __gt__(self, other):

    # ==
    def __eq__(self, other):
        if self.x == other.x:
            print(True)
        else:
            print(False)

v1 = Vector(22, 22)
v2 = Vector(23, 23)
v3 = v2 + v1
v4 = v1 < v2
v5 = v1 == v2