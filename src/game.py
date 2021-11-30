import pygame
from entities import Player
from src.dialog import DialogBox
from src.map import MapManager


class Game:
    def __init__(self):
        # Start
        self.running = True

        # Game screen
        flags = pygame.NOFRAME | pygame.FULLSCREEN | pygame.SCALED
        self.screen = pygame.display.set_mode((800, 600), flags, vsync=1)
        pygame.display.set_caption('Game')

        # Create the player
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        inputs = pygame.Vector2(0, 0)
        if pressed[pygame.K_ESCAPE]:
            self.running = False
        if pressed[pygame.K_z]:
            inputs.y -= 1
        if pressed[pygame.K_s]:
            inputs.y += 1
        if pressed[pygame.K_d]:
            inputs.x += 1
        if pressed[pygame.K_q]:
            inputs.x -= 1
        self.player.move(inputs)

    def update(self):
        self.map_manager.update()

    def run(self):
        clock = pygame.time.Clock()

        # Clock
        while self.running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            self.dialog_box.render(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.map_manager.check_npc_collisions(self.dialog_box)

            clock.tick(60)

        pygame.quit()
