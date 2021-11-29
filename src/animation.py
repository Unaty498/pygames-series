import pygame


class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'../sprites/{name}.png')
        self.animation_index = 0
        self.clock = 0
        self.images = {
            'down': self.get_images(0),
            'left': self.get_images(32),
            'right': self.get_images(64),
            'up': self.get_images(96)
        }
        self.speed = 1

    def change_animation(self, name):
        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey(0, 0)
        self.clock += self.speed * 8

        if self.clock >= 100:
            self.animation_index += 1  # Go to the next image

            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0

            self.clock = 0

    def get_images(self, y):
        return [self.get_image(x*32, y).convert_alpha() for x in range(4)]

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
