import pygame

semua_kunci = pygame.sprite.Group()

class Kunci(pygame.sprite.Sprite):
    def __init__(self, x, y, warna):
        super(Kunci, self).__init__()
        self.kunci = pygame.image.load("./Assets/Img/Kunci/kunci_putih.png")
        self.rect = self.kunci.convert_alpha().get_rect()
        self.rect.center = (x, y)
        semua_kunci.add(self)
    
    def update(self, screen, offset):
        screen.blit(self.kunci, (self.rect[0] - offset[0], self.rect[1] - offset[1]))