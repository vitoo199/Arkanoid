import src.Paddle as Paddle
import pygame as pg


def test_should_not_pass_over_the_left_edge():
    surface = pg.Surface((800, 600))
    paddle = Paddle.Paddle((0, 550), (200, 20))
    paddle.speed = 10
    paddle.dir_left = True
    paddle.update(surface)
    assert paddle.left >= 0


def test_should_not_pass_over_the_right_edge():
    surface = pg.Surface((800, 600))
    paddle = Paddle.Paddle((0, 550), (200, 20))
    paddle.speed = 10
    paddle.dir_right = True
    paddle.update(surface)
    w, h = surface.get_size()
    assert paddle.right <= w
