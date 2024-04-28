import pygame
import math
from .Peti import semua_peti
from .Dinding import semua_dinding

class Pemain(pygame.sprite.Sprite):
    pemain_x = 16
    pemain_y = 36

    gerak_kiri = False
    gerak_kanan = False
    gerak_atas = False
    gerak_bawah = False
    gerak_count = 0
    
    animasi_diam = pygame.image.load("./Assets/Img/Pemain/Diam.png")
    animasi_kiri = [pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri1.png"), pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri2.png"),pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri3.png"),pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri4.png"),pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri5.png"),pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri6.png"),pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri7.png"),pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri8.png")]
    animasi_kanan = [pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan1.png"), pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan2.png"),pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan3.png"),pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan4.png"),pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan5.png"),pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan6.png"), pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan7.png"), pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan8.png")]

    def __init__(self):
        super(Pemain, self).__init__()
        self.rect = self.animasi_diam.convert_alpha().get_rect()
        self.rect.width -= 16
        self.rect.height -= 16
        self.is_pemain_touch_peti = pygame.sprite.spritecollide(self, semua_peti, False)
        self.is_pemain_touch_dinding  = pygame.sprite.spritecollide(self, semua_dinding, False)

    def update(self, screen):
        self.rect.center = (self.pemain_x + 16, self.pemain_y + 24)
        self.is_pemain_touch_peti = pygame.sprite.spritecollide(self, semua_peti, False)
        self.is_pemain_touch_dinding = pygame.sprite.spritecollide(self, semua_dinding, False)

        # pygame.draw.rect(screen, "Red", self.rect)
        if self.is_pemain_touch_dinding:
            for dinding in self.is_pemain_touch_dinding:
                dinding_rect = dinding.rect
                if self.rect.right > dinding_rect.left and self.rect.left < dinding_rect.left:
                    self.gerak(-3, 0)
                elif self.rect.left < dinding_rect.right and self.rect.right > dinding_rect.right:
                    self.gerak(3, 0)
                if self.rect.bottom > dinding_rect.top and self.rect.top < dinding_rect.top:
                    self.gerak(0, -3)
                elif self.rect.top < dinding_rect.bottom and self.rect.bottom > dinding_rect.bottom:
                    self.gerak(0, 3)
         
        if self.is_pemain_touch_peti:
            for peti in self.is_pemain_touch_peti:
                peti_rect = peti.rect
                if self.rect.right > peti_rect.left and self.rect.left < peti_rect.left:
                    self.gerak(-3, 0)
                elif self.rect.left < peti_rect.right and self.rect.right > peti_rect.right:
                    self.gerak(3, 0)
                elif self.rect.bottom > peti_rect.top and self.rect.top < peti_rect.top:
                    self.gerak(0, -3)
                elif self.rect.top < peti_rect.bottom and self.rect.bottom > peti_rect.bottom:
                    self.gerak(0, 3)

        if self.gerak_count >= 21:
            self.gerak_count = 0

        if self.gerak_kiri == True:
            self.gerak(-3, 0)
            self.gerak_count += 1
        elif self.gerak_kanan == True:
            self.gerak(3, 0)
            self.gerak_count += 1
        if self.gerak_bawah == True:
            self.gerak(0, 3)
            self.gerak_count += 1
        elif self.gerak_atas == True:
            self.gerak(0, -3)
            self.gerak_count += 1

        if self.gerak_kiri == True:
            screen.blit(self.animasi_kiri[self.gerak_count // 3], (self.pemain_x, self.pemain_y))
        elif self.gerak_kanan == True:
            screen.blit(self.animasi_kanan[self.gerak_count // 3], (self.pemain_x, self.pemain_y))
        elif self.gerak_bawah == True:
            screen.blit(self.animasi_kiri[self.gerak_count // 3], (self.pemain_x, self.pemain_y))
        elif self.gerak_atas == True:
            screen.blit(self.animasi_kiri[self.gerak_count // 3], (self.pemain_x, self.pemain_y))
        else:
            screen.blit(self.animasi_diam, (self.pemain_x, self.pemain_y))


    def isAbleToInteract(self, x, y):
        distance = math.sqrt(math.pow(self.pemain_x - x, 2) + (math.pow(self.pemain_y - y, 2)))
        if distance < 27:
            return True
        else:
            return False

    def gerak(self, x, y):
        self.pemain_x += x
        self.pemain_y += y