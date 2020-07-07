
class Game:
    '''Controlls current Game State'''

    def __init__(self, init_state=None, menu_state=None, game_playing_state=None):
        self.state = init_state
        self.init_state = init_state
        self.menu_state = menu_state
        self.game_playing_state = game_playing_state

    def _set_state(self, state=None):
        if state:
            self.state = state

    def run(self):
        if self.state:
            self.state.on_enter()
            self.state.run()
