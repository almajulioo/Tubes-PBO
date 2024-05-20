import pygame
import math
from .Peti import semua_peti
from .Dinding import semua_dinding
from .Kunci import semua_kunci

class Pemain(pygame.sprite.Sprite):
    pemain_pos = [19,42]

    gerak_kiri = False
    gerak_kanan = False
    gerak_atas = False
    gerak_bawah = False
    gerak_count = 0

    
    animasi_diam = pygame.image.load("./Assets/Img/Pemain/Diam.png")

    animasi_kanan = [pygame.image.load("./Assets/Img/Pemain/Mov/1.png"), pygame.image.load("./Assets/Img/Pemain/Mov/2.png"),pygame.image.load("./Assets/Img/Pemain/Mov/3.png"),pygame.image.load("./Assets/Img/Pemain/Mov/4.png"),pygame.image.load("./Assets/Img/Pemain/Mov/5.png"),pygame.image.load("./Assets/Img/Pemain/Mov/6.png"), pygame.image.load("./Assets/Img/Pemain/Mov/7.png"), pygame.image.load("./Assets/Img/Pemain/Mov/8.png")]

    animasi_kiri = []

    kunci_terambil = 0

    for i in animasi_kanan:
        animasi_kiri.append(pygame.transform.flip(i,True,False))

    def __init__(self):
        super(Pemain, self).__init__()
        self.rect = self.animasi_diam.convert_alpha().get_rect()
        self.rect.width -= 16
        self.rect.height -= 16
        self.is_pemain_touch_peti = pygame.sprite.spritecollide(self, semua_peti, False)
        self.is_pemain_touch_dinding  = pygame.sprite.spritecollide(self, semua_dinding, False)
        self.fog = pygame.Surface((400, 300)).convert_alpha()
        self.fog_vision = 50
        self.move_speed = 3

    def update(self, screen, offset=(0,0)):
        self.rect.center = (self.pemain_pos[0] + 16, self.pemain_pos[1] + 24)
        self.is_pemain_touch_peti = pygame.sprite.spritecollide(self, semua_peti, False)
        self.is_pemain_touch_dinding = pygame.sprite.spritecollide(self, semua_dinding, False)
        self.is_pemain_touch_kunci = pygame.sprite.spritecollide(self, semua_kunci, False)
        
        #pygame.draw.rect(screen, "Red", self.rect)
        # Menangani kondisi jika pemain menyentuh atau menabrak dinding
        if self.is_pemain_touch_dinding:
            # tangani gerakan horizontal
            if self.gerak_kiri or self.gerak_kanan:
                for dinding in self.is_pemain_touch_dinding:
                    dinding_rect = dinding.rect
                    if self.gerak_kiri and self.rect.left < dinding_rect.right and self.rect.right > dinding_rect.right:
                        self.gerak(self.move_speed, 0)
                    elif self.gerak_kanan and self.rect.right > dinding_rect.left and self.rect.left < dinding_rect.left:
                        self.gerak(-self.move_speed, 0)

            # tangani gerakan vertikal
            if self.gerak_atas or self.gerak_bawah:
                for dinding in self.is_pemain_touch_dinding:
                    dinding_rect = dinding.rect
                    if self.gerak_atas and self.rect.top < dinding_rect.bottom and self.rect.bottom > dinding_rect.bottom:
                        self.gerak(0, self.move_speed)
                    elif self.gerak_bawah and self.rect.bottom > dinding_rect.top and self.rect.top < dinding_rect.top:
                        self.gerak(0, -self.move_speed)

        # Menangani kondisi jika pemain menyentuh atau menabrak peti
        if self.is_pemain_touch_peti:
            for peti in self.is_pemain_touch_peti:
                peti_rect = peti.rect
                if self.rect.right > peti_rect.left and self.rect.left < peti_rect.left:
                    self.gerak(-self.move_speed, 0)
                elif self.rect.left < peti_rect.right and self.rect.right > peti_rect.right:
                    self.gerak(self.move_speed, 0)
                elif self.rect.bottom > peti_rect.top and self.rect.top < peti_rect.top:
                    self.gerak(0, -self.move_speed)
                elif self.rect.top < peti_rect.bottom and self.rect.bottom > peti_rect.bottom:
                    self.gerak(0, self.move_speed)

        # Menangani kondisi jika pemain menyentuh atau menabrak kunci
        if self.is_pemain_touch_kunci:
            for kunci in self.is_pemain_touch_kunci:
                self.kunci_terambil += 1
                kunci.terambil = True
                
        if self.gerak_count >= 21:
            self.gerak_count = 0

        # Menangani gerakan pemain
        dx = 0
        dy = 0

        if self.gerak_kiri:
            dx -= self.move_speed
        if self.gerak_kanan:
            dx += self.move_speed
        if self.gerak_atas:
            dy -= self.move_speed
        if self.gerak_bawah:
            dy += self.move_speed

        if dx != 0 and dy != 0:
            factor = 1 / 1.414 
            dx *= factor
            dy *= factor
            
        self.gerak(dx, dy)
        if dx != 0 or dy != 0:
            self.gerak_count += 1

        # Menangani animasi pemain dan kamera
        if self.gerak_kiri == True:
            screen.blit(self.animasi_kiri[self.gerak_count // 3], (self.pemain_pos[0] - offset[0] , self.pemain_pos[1] - offset[1]))
        elif self.gerak_kanan == True:
            screen.blit(self.animasi_kanan[self.gerak_count // 3], (self.pemain_pos[0] - offset[0], self.pemain_pos[1] - offset[1]))
        elif self.gerak_bawah == True:
            screen.blit(self.animasi_kiri[self.gerak_count // 3], (self.pemain_pos[0] - offset[0], self.pemain_pos[1] - offset[1]))
        elif self.gerak_atas == True:
            screen.blit(self.animasi_kiri[self.gerak_count // 3], (self.pemain_pos[0] - offset[0], self.pemain_pos[1] - offset[1]))
        else:
            screen.blit(self.animasi_diam, (self.pemain_pos[0] - offset[0], self.pemain_pos[1] - offset[1]))

        
        self.fog.fill((7,7,10))
        pygame.draw.circle(self.fog, (0,0,0,50), (self.rect.centerx - offset[0], self.rect.centery - offset[1]), self.fog_vision)
        
        screen.blit(self.fog, (0,0))

    # Fungsi apabila pemain sudah diperbolehkan melakukan interaksi dengan objek lain
    def isAbleToInteract(self, pos):
        distance = math.sqrt(math.pow(self.pemain_pos[0] - pos[0], 2) + (math.pow(self.pemain_pos[1] - pos[1], 2)))
        if distance < 32:
            return True
        else:
            return False
        
    # Fungsi untuk menangani perubahan posisi pemain berdasarkan gerakan
    def gerak(self, x, y):
        self.pemain_pos[0] += x
        self.pemain_pos[1] += y