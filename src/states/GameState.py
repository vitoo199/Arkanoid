import abc


class GameState(abc.ABC):
    '''Abstract Game State'''

    def __init__(self, game):
        self.game = game

    @abc.abstractmethod
    def on_enter(self):
        pass

    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def exit(self):
        pass
