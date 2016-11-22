class City(object):
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y

    def __str__(self):
        return self.label + " " + self.x + " " + self.y