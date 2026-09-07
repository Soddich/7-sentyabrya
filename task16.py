import random

class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

classes = [Line, Rect, Ellipse]

elements = []

for _ in range(217):
    cls = random.choice(classes)
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, 100)
    d = random.randint(1, 100)
    obj = cls(a, b, c, d)
    elements.append(obj)

for obj in elements:
    if isinstance(obj, Line):
        obj.sp = (0, 0)
        obj.ep = (0, 0)