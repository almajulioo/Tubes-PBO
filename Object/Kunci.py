import pygame

semua_kunci = pygame.sprite.Group()

class Kunci(pygame.sprite.Sprite):
    terambil = False

    def __init__(self, x, y, warna):
        super(Kunci, self).__init__()
        self.kunci = pygame.image.load("./Assets/Img/Kunci/kunci_putih.png")
        self.kunci.set_colorkey((0,0,0))
        self.rect = self.kunci.convert_alpha().get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        semua_kunci.add(self)
    
    def update(self, screen, offset):
        # pygame.draw.rect(screen, "Red", self.rect)
        screen.blit(self.kunci, (self.rect[0] - offset[0], self.rect[1] - offset[1]))
        if self.terambil == True:
            self.rect.centerx = 10000
    
    def reset(self):
        self.rect.center = (self.x, self.y)
        self.terambil = False
    