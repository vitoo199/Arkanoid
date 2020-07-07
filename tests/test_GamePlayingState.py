import src.Ball as Ball
import pygame as pg
import src.Paddle as Paddle
import src.states.GamePlayingState as GamePlayingState
import src.Screen as Screen


def test_ball_should_bounce_from_paddle():
    ball = Ball.Ball((400, 560), (10, 10))
    paddle = Paddle.Paddle((400, 550), (200, 20))
    g_playing_state = GamePlayingState.GamePlayingState(
        Screen.Screen((800, 600), pg.display), ball, paddle)
    g_playing_state.collision()
    assert ball.speed.y < 0


def test_ball_should_bounce_from_block():
    ball = Ball.Ball((400, 560), (10, 10))
    paddle = Paddle.Paddle((400, 550), (200, 20))
    g_playing_state = GamePlayingState.GamePlayingState(
        Screen.Screen((800, 600), pg.display), ball, paddle)
    ball.left = g_playing_state.blocks[-1].left
    ball.right = g_playing_state.blocks[-1].right
    g_playing_state.collision()
    assert ball.speed.y > 0
