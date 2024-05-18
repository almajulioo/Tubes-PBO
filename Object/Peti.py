import pygame

semua_peti = pygame.sprite.Group()
list_semua_peti = semua_peti.sprites()

class Peti(pygame.sprite.Sprite):
    animasi_diam = pygame.image.load("./Assets/Img/Peti/diam.png")
    animasi_buka = [pygame.image.load("./Assets/Img/Peti/Peti1.png"), pygame.image.load("./Assets/Img/Peti/Peti2.png"), pygame.image.load("./Assets/Img/Peti/Peti3.png"), pygame.image.load("./Assets/Img/Peti/Peti4.png"), pygame.image.load("./Assets/Img/Peti/Peti5.png"), pygame.image.load("./Assets/Img/Peti/Peti6.png"), pygame.image.load("./Assets/Img/Peti/Peti7.png"), pygame.image.load("./Assets/Img/Peti/Peti8.png"), pygame.image.load("./Assets/Img/Peti/Peti9.png"), pygame.image.load("./Assets/Img/Peti/Peti10.png")]
    animasi_count = 0

    buka = False
    
    def __init__(self, x, y):
        super(Peti, self).__init__()
        self.peti_x = x 
        self.peti_y = y
        self.rect = self.animasi_diam.convert_alpha().get_rect()
        self.rect.center = (self.peti_x, self.peti_y)
        semua_peti.add(self)


    def update(self, screen, offset=(0,0)):
            # pygame.draw.rect(screen, "Red", self.rect)

            if self.animasi_count == 27:
                self.buka = False
                self.animasi_diam = pygame.image.load("./Assets/Img/Peti/Peti10.png")


            if self.buka == True:
                self.animasi_count += 1 
                screen.blit(self.animasi_buka[self.animasi_count // 3], (self.rect[0] - offset[0], self.rect[1] - offset[1]))
            else:  
                screen.blit(self.animasi_diam, (self.rect[0] - offset[0], self.rect[1] - offset[1]))

            
