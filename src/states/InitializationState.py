import src.states.GameState as GameState
import pygame as pg
import src.Screen as Screen


class InitializationState(GameState.GameState):
    '''Represents Initialization State '''

    # def __init__(self, game):
    #     super().__init__(game)
    def on_enter(self):
        pass

    def run(self):
        pg.init()
        self.exit()

    def exit(self):
        self.game._set_state(self.game.menu_state)
        self.game.run()
