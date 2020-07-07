import src.states.GameState as GameState
import pygame as pg
import src.Screen as Screen
import sys


class MainMenuState(GameState.GameState):
    '''Represents Main Menu State '''

    def __init__(self, game):
        super().__init__(game)
        pg.init()
        self.font = pg.font.SysFont('dejavuserif', 30)
        self.screen = Screen.Screen((800, 600), pg.display)

        self.play_btn_text = None
        self.play_btn = None

        self.exit_btn_text = None
        self.exit_btn = None
        
    def on_enter(self):
        self.play_btn_text = self.font.render('Play', True, pg.Color('red'))
        self.play_btn = self.play_btn_text.get_rect(
            topleft=(400 - self.font.size('Play')[0]/2, 100))

        self.exit_btn_text = self.font.render('Exit', True, pg.Color('red'))
        self.exit_btn = self.exit_btn_text.get_rect(
            topleft=(400 - self.font.size('Exit')[0]/2, 200))

    def run(self):
        pg.init()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.exit()
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pg.mouse.get_pos()
                    if self.play_btn.collidepoint(mouse_x, mouse_y):
                        self.on_play_clicked()
                    if self.exit_btn.collidepoint(mouse_x, mouse_y):
                        self.exit()
                self.screen.fill()
                self.screen.surface.blit(self.play_btn_text, self.play_btn)
                self.screen.surface.blit(self.exit_btn_text, self.exit_btn)

                pg.display.flip()

    def on_play_clicked(self) -> None:
        self.game._set_state(self.game.game_playing_state)
        self.game.run()

    def exit(self) -> None:
        pg.quit()
        sys.exit()
