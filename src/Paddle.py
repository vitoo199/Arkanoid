import pygame as pg


class Paddle(pg.Rect):
    '''Represents Paddle in the Game'''

    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.speed = 1
        self.dir_right = False
        self.dir_left = False

    def draw(self):
        pg.draw.rect(pg.display.get_surface(), (0, 255, 0), self)
