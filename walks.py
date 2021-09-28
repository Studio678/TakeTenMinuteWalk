"""
You live in the city of Cartesia where all roads are laid out in a perfect grid.
You arrived ten minutes too early to an appointment, so you decided to take the opportunity
to go for a short walk.
The city provides its citizens with a Walk Generating App on their phones -- everytime
you press the button it sends you an array of one-letter strings
representing directions to walk (eg. ['n', 's', 'w', 'e']).
You always walk only a single block for each letter (direction) and
you know it takes you one minute to traverse one city block, so create a function that will
return true if the walk the app gives you will take you exactly ten minutes
(you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

    Note: you will always receive a valid array containing a random
    assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!)
"""


class Walks:
    max_long_of_walk: int = 10

    def __init__(self, walk):
        if walk is None:
            self.walk = []
        else:
            self.walk = walk
        self.startX: int = 0
        self.startY: int = 0
        self.x = self.startX
        self.y = self.startY
        self.point = [self.x, self.y]
        self.directions = {
            'n': self.point.insert(self.point[0], self.point[1] + 1),
            's': self.point.insert(self.point[0], self.point[1] - 1),
            'e': self.point.insert(self.point[0] + 1, self.point[1]),
            'w': self.point.insert(self.point[0] - 1, self.point[1])
        }

    def is_valid_walk(self):
        # determine if walk is valid
        long_of_walk = len(self.walk)

        if long_of_walk == Walks.max_long_of_walk:
            for move in self.walk:
                try:
                    self.point = self.directions[move]
                except KeyError as e:
                    # set default error value
                    raise ValueError('Undeclared unit: {}'.format(e.args[0]))
            if self.startX == self.point[0] and self.startY == self.point[1]:
                return True
        else:
            return False
