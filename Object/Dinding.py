import pygame

semua_dinding = pygame.sprite.Group()

class Dinding(pygame.sprite.Sprite):
    def __init__(self, x, y, sisi):
        pygame.sprite.Sprite.__init__(self)
        if sisi == "atas":
            self.dinding = pygame.image.load("./Assets/Img/Dinding/dinding_atas.png")
        elif sisi == "bawah":
            self.dinding = pygame.image.load("./Assets/Img/Dinding/dinding_bawah.png")
        elif sisi == "bawah2":
            self.dinding = pygame.image.load("./Assets/Img/Dinding/dinding_bawah2.png")
        elif sisi == "kanan" or sisi == "kiri":
            self.dinding = pygame.image.load("./Assets/Img/Dinding/dinding_kiri.png")
        elif sisi == "kanan2" or sisi == "kiri2":
            self.dinding = pygame.image.load("./Assets/Img/Dinding/dinding_kiri2.png")
        self.rect = self.dinding.convert_alpha().get_rect()
        self.rect.center = (x, y)
        semua_dinding.add(self)

    def update(self, screen):
        screen.blit(self.dinding, self.rect)
        # pygame.draw.rect(screen, "Red", self.rect)
