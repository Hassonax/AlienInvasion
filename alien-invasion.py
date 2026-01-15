import sys 

import pygame

from settings import Settings
from ship import Ship

# Source - https://stackoverflow.com/a
# Posted by Freddy Mcloughlan, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-30, License - CC BY-SA 4.0


class AlienInvasion :
    """overall class to manage game assests and behaviour"""

    def __init__(self):
        """initialize the game , and create game resources"""
        pygame.init()

        #self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien invasion")
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        self.moving_right = False


    def update(self):
        if self.moving_right :
            self.rect.x += 1

        #self.bg_color = (230,230,230)i

    def run_game(self) :
        """start the main loop for the game"""
        while True : 
            

            self._check_events()
            self.ship.update()
            #watch for keybourd and  mouse events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         sys.exit()

            self._update_screen()
            self.clock.tick(60)
                    #make game most recently draw vissable on the screen
            pygame.display.flip()
            
            
            #redraw the screen during each pass throgh the look
            
            # self.screen.fill(self.settings.bg_color)
            # self.ship.blitme()
    

    def _check_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                    # self.ship.rect.x += 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT :
                        self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.rect.x -= 1


    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()



if __name__ == '__main__' :

    ai = AlienInvasion()
    ai.run_game()
        
