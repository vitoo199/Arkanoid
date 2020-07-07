import sys

import pygame as pg

import src.states.GameState as GameState


class GamePlayingState(GameState.GameState):
    '''Represents Game Playing State.'''

    def __init__(self, game, screen, ball, paddle):
        super().__init__(game)
        pg.init()
        self.screen = screen
        self.ball = ball
        self.paddle = paddle
        self.clock = pg.time.Clock()
        self.BLOCK_SIZE = pg.Vector2(100, 20)
        self.blocks = []

    def on_enter(self):
        self.blocks = [pg.Rect(pg.Vector2(
            (j * (self.BLOCK_SIZE.x + 50) + 50), (i*(self.BLOCK_SIZE.y + 50))), self.BLOCK_SIZE) for i in range(3) for j in range(self.screen.surface.get_size()[0] // int(self.BLOCK_SIZE.x + 50))]

    def run(self):
        pg.init()
        self._loop()

    def proccess_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    self.paddle.dir_right = True
                if event.key == pg.K_a:
                    self.paddle.dir_left = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_d:
                    self.paddle.dir_right = False
                if event.key == pg.K_a:
                    self.paddle.dir_left = False

    def update(self):
        self.ball.update(self.screen.surface)

    def draw(self):
        self.ball.draw()
        self.paddle.draw()
        for block in self.blocks:
            pg.draw.rect(self.screen.surface, (0, 0, 255), block)

    def _loop(self):
        while True:
            self.proccess_events()
            self.screen.fill()

            self.update()
            if not len(self.blocks):
                self.game._set_state(self.game.menu_state)
                self.game.run()
            self.collision()
            self.draw()
            self.paddle.left = self.ball.left - 50

            pg.display.flip()
            self.clock.tick(200)

    def collision(self):
        if self.paddle.colliderect(self.ball):
            self.ball.speed.y *= -1
        collide_index = self.ball.collidelist(self.blocks)
        if collide_index != -1:
            self.blocks.pop(collide_index)
            self.ball.speed.y *= -1

        w, h = self.screen.surface.get_size()
        if self.ball.right >= w or self.ball.left <= 0:
            self.ball.speed.x *= -1
        if self.ball.top <= 0:
            self.ball.speed.y *= -1
        if self.ball.bottom >= h:
            self.exit()

        if self.paddle.dir_right and self.paddle.right + self.paddle.speed <= w:
            self.paddle.move_ip((self.paddle.speed, 0))
        if self.paddle.dir_left and self.paddle.left - self.paddle.speed >= 0:
            self.paddle.move_ip((-self.paddle.speed, 0))

    def exit(self):
        pg.quit()
        sys.exit()
