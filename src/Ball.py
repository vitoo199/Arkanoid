import pygame as pg


class Ball(pg.Rect):
    '''Represents Ball in the game'''

    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.speed = pg.Vector2(1, 1)

    def update(self, surface):
        self.move_ip(int(self.speed.x), int(self.speed.y))

    def draw(self):
        pg.draw.rect(pg.display.get_surface(), (255, 0, 0), self)
