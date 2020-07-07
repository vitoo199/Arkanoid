

class Screen:
    '''Represents Screen in the Game.'''

    def __init__(self, size, display, background=(0, 0, 0)):
        self.surface = display.set_mode(size)
        self.background = background

    def fill(self):
        '''Fills the screen'''

        self.surface.fill(self.background)

    def draw(self, obj):
        '''Draws screen '''
        obj.draw(self.surface)
