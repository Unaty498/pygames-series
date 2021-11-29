import pygame


class DialogBox:
    def __init__(self):
        self.box = pygame.image.load('./dialogs/dialog_box.png')
        self.box = pygame.transform.scale(self.box, (700, 100))
        self.texts = []
        self.text_index = 0
        self.letter_index = 0
        self.font = pygame.font.Font('./dialogs/dialog_font.ttf', 18)
        self.reading = False
        self.Y_POSITION = pygame.display.get_surface().get_height() - self.box.get_height()
        self.X_POSITION = pygame.display.get_surface().get_width() - self.box.get_width()

    def execute(self, dialog=[]):
        if self.reading:
            self.next_text()
        else:
            self.reading = True
            self.text_index = 0
            self.texts = dialog

    def render(self, screen):
        if self.reading:
            self.letter_index += 1

            if self.letter_index >= len(self.texts[self.text_index]):
                self.letter_index = self.letter_index

            screen.blit(self.box, (self.X_POSITION - 40, self.Y_POSITION))
            text = self.font.render(self.texts[self.text_index][0:self.letter_index], False, (0, 0, 0))
            screen.blit(text, (self.X_POSITION + 60, self.Y_POSITION + 30))

    def next_text(self):
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            # Close dialog
            self.reading = False