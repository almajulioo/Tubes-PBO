import pygame

semua_dinding = pygame.sprite.Group()

class Dinding(pygame.sprite.Sprite):
    def __init__(self, x, y, sisi):
        super(Dinding, self).__init__()
        if sisi == "atas":
            self.dinding = pygame.image.load("./Assets/Img/Dinding/dinding_atas.png")
        elif sisi == "bawah":
            self.dinding = pygame.image.load("./Assets/Img/Dinding/dinding_bawah.png")
        elif sisi == "bawah2":
            self.dinding = pygame.image.load("./Assets/Img/Dinding/dinding_bawah2.png")
        elif sisi == "kiri":
            self.dinding = pygame.image.load("./Assets/Img/Dinding/dinding_kiri.png")
        elif sisi == "kiri2":
            self.dinding = pygame.image.load("./Assets/Img/Dinding/dinding_kiri2.png")
        elif sisi == "kanan":
            self.dinding = pygame.image.load("./Assets/Img/Dinding/dinding_kanan.png")
        elif sisi == "kanan2":
            self.dinding = pygame.image.load("./Assets/Img/Dinding/dinding_kanan2.png")
        elif sisi == "penghubung":
            self.dinding = pygame.image.load("./Assets/Img/Dinding/penghubung.png")
        elif sisi == "dinding_full":
            self.dinding = pygame.image.load("./Assets/Img/Dinding/dinding_full.png")
       
       
        self.rect = self.dinding.convert_alpha().get_rect()
        self.rect.center = (x, y)
        semua_dinding.add(self)

    def update(self, screen, offset=(0,0)): 
        screen.blit(self.dinding, (self.rect[0] - offset[0], self.rect[1] - offset[1]))
        #pygame.draw.rect(screen, "Red", self.rect)
