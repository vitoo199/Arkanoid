import src.Ball as Ball
import pygame as pg
import src.Paddle as Paddle


def test_should_bounce_from_right_wall():
    surf = pg.Surface((800, 600))
    ball = Ball.Ball((790, 500), (10, 10))
    ball.speed = pg.Vector2(10, 1)
    is_moving_right = ball.speed.x > 0
    ball.move_ip(int(ball.speed.x), int(ball.speed.y))
    ball.update(surf)
    is_moving_right = ball.speed.x > 0

    assert not is_moving_right


def test_should_bounce_from_left_wall():
    surf = pg.Surface((800, 600))
    ball = Ball.Ball((10, 500), (10, 10))
    ball.speed = pg.Vector2(-10, 1)
    is_moving_left = ball.speed.x < 0
    ball.move_ip(int(ball.speed.x), int(ball.speed.y))
    ball.update(surf)
    is_moving_left = ball.speed.x < 0

    assert not is_moving_left


def test_should_bounce_from_top_wall():
    surf = pg.Surface((800, 600))
    ball = Ball.Ball((500, 100), (10, 10))
    ball.speed = pg.Vector2(-10, 100)
    is_moving_top = ball.speed.y < 0
    ball.move_ip(int(ball.speed.x), int(ball.speed.y))
    ball.update(surf)
    is_moving_top = ball.speed.y < 0

    assert not is_moving_top


def test_should_bounce_from_bottom_wall():
    surf = pg.Surface((800, 600))
    ball = Ball.Ball((500, 500), (10, 10))
    ball.speed = pg.Vector2(-10, 100)
    is_moving_bottom = ball.speed.y > 0
    ball.move_ip(int(ball.speed.x), int(ball.speed.y))
    ball.update(surf)
    is_moving_bottom = ball.speed.y > 0

    assert not is_moving_bottom
