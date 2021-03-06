import pygame


class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.sprite_sheet = pygame.image.load(f'../sprites/{name}.png')
        self.current_animation = 'down'
        self.animation_index = 0
        self.clock = 0
        self.images = {
            'down': self.get_images(0),
            'left': self.get_images(32),
            'right': self.get_images(64),
            'up': self.get_images(96)
        }
        self._speed = 10

    def change_animation(self, name):
        self.current_animation = name
        self.animation_index = 0
        self.clock = 0

    def tick_animation(self):
        self.clock -= 1
        if self.clock < 0:
            self.animation_index += 1  # Go to the next image
            self.animation_index %= len(self.images[self.current_animation])
            self.image = self.images[self.current_animation][self.animation_index]
            self.image.set_colorkey(0, 0)
            self.clock = self._speed

    def get_images(self, y):
        return [self.get_image(x*32, y).convert_alpha() for x in range(4)]

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
