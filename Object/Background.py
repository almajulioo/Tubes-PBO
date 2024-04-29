import pygame

semua_background = pygame.sprite.Group()

class Background(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Background, self).__init__()
        self.background = pygame.image.load("./Assets/Img/Background/background.png")
        self.background_x = x
        self.background_y = y
        semua_background.add(self)

    def update(self, screen):
        screen.blit(self.background, (self.background_x, self.background_y))
