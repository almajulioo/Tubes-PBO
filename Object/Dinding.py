import pygame

semua_dinding = pygame.sprite.Group()

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./Assets/Img/Dinding/Dinding.png")

        self.rect = self.image.convert_alpha().get_rect()
        # self.rect.width += 100
        self.rect.center = (x, y)
        semua_dinding.add(self)

    def update(self, screen):
        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen, "Red", self.rect)
