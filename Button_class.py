from Sprite import Sprite


class Button(Sprite):
    def __init__(self, x, y, box_X=500, box_Y=120):
        super().__init__(x, y, 0)
        self.rect.update((self.X, self.Y), (box_X, box_Y))
