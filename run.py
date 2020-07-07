import src.Game as Game
import src.containers.States as States

import src.Screen as Screen
import src.Ball as Ball
import src.Paddle as Paddle

import pygame as pg
if __name__ == "__main__":
    game = Game.Game()
    game.__init__(States.GameStates.init_state(game), States.GameStates.menu_state(game), States.GameStates.game_playing_state(game,
                                                                                                                               Screen.Screen(
                                                                                                                                   (800, 600), pg.display, (0, 0, 0)),
                                                                                                                               Ball.Ball(
                                                                                                                                   (300, 300), (10, 10)),
                                                                                                                               Paddle.Paddle(((800 / 2) - 200/2, 550), (100, 10))))
    game.run()
