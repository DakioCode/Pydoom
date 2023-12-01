import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen : pygame.Surface) -> None:
        super.__init__(super())
        
        self.screen = screen

        self.speed = 10
        self.position = {
            "x": 150,
            "y": 150
        }

        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()

    def move_up(self) -> None: self.position["y"] -= self.speed
    def move_down(self) -> None: self.position["y"] += self.speed
    def move_left(self) -> None: self.position["x"] -= self.speed
    def move_right(self) -> None: self.position["x"] += self.speed

    def draw(self) -> None:
        self.screen.blit(self.image, (self.position["x"], self.position["y"]))
        if self.position['x'] >= self.screen.get_size()[0] \
        or self.position['x'] < 0 \
        or self.position['y'] >= self.screen.get_size()[1] \
        or self.position['y'] < 0:
            self.position['x'] = self.screen.get_size()[0] / 2
            self.position['y'] = self.screen.get_size()[1] / 2