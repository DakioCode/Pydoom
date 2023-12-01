import pygame
from player import Player

class Game:
    def __init__(self) -> None:
        pygame.init()

        pygame.display.set_mode((780, 500))
        pygame.display.set_caption("Pydoom - RPG")

        self.screen = pygame.display.get_surface()

        self.clock = pygame.time.Clock()

        self.player = Player(self.screen)

        self.running = True

    def handle_inputs(self) -> None:
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]: self.player.move_up()
        if pressed[pygame.K_DOWN]: self.player.move_down()
        if pressed[pygame.K_LEFT]: self.player.move_left()
        if pressed[pygame.K_RIGHT]: self.player.move_right()
        if pressed[pygame.K_f]: print(f"{self.player.position} / {self.screen.get_size()}")

    def run(self) -> None:
        while self.running:
            self.player.draw()

            self.handle_inputs()

            pygame.display.update()
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.running = False
                    break

            self.clock.tick(60)