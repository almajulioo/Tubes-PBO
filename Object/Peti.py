import pygame

semua_peti = pygame.sprite.Group()
list_semua_peti = semua_peti.sprites()

class Peti(pygame.sprite.Sprite):
    peti_x = 700
    peti_y = 0

    animasi_diam = pygame.image.load("./Assets/Img/Peti/Peti1.png")
    animasi_buka = [pygame.image.load("./Assets/Img/Peti/Peti1.png"), pygame.image.load("./Assets/Img/Peti/Peti2.png"), pygame.image.load("./Assets/Img/Peti/Peti3.png"), pygame.image.load("./Assets/Img/Peti/Peti4.png"), pygame.image.load("./Assets/Img/Peti/Peti5.png"), pygame.image.load("./Assets/Img/Peti/Peti6.png"), pygame.image.load("./Assets/Img/Peti/Peti7.png"), pygame.image.load("./Assets/Img/Peti/Peti8.png"), pygame.image.load("./Assets/Img/Peti/Peti9.png"), pygame.image.load("./Assets/Img/Peti/Peti10.png")]
    animasi_count = 0


    buka = False
    
    def __init__(self):
        super(Peti, self).__init__()
        self.rect = self.animasi_diam.convert_alpha().get_rect()
        self.rect.width -= 24
        self.rect.height -= 16
        semua_peti.add(self)


    def update(self, screen):
            self.rect.center = (self.peti_x + 16, self.peti_y + 24)
            # pygame.draw.rect(screen, "Red", self.rect)

            if self.animasi_count == 27:
                self.buka = False
                self.animasi_diam = pygame.image.load("./Assets/Img/Peti/Peti10.png")
                
            if self.buka == True:
                self.animasi_count += 1 
                screen.blit(self.animasi_buka[self.animasi_count // 3], (self.peti_x, self.peti_y))
            else:  
                screen.blit(self.animasi_diam, (self.peti_x, self.peti_y))
