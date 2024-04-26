import pygame
import math

class Pemain:
    pemain_x = 100
    pemain_y = 0
    kecepatan_x = 3

    gerak_kiri = False
    gerak_kanan = False
    gerak_count = 0

    animasi_diam = pygame.image.load("./Assets/Img/Pemain/Diam.png")
    animasi_kiri = [pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri1.png"), pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri2.png"),pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri3.png"),pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri4.png"),pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri5.png"),pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri6.png"),pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri7.png"),pygame.image.load("./Assets/Img/Pemain/Kiri/Kiri8.png")]
    animasi_kanan = [pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan1.png"), pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan2.png"),pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan3.png"),pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan4.png"),pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan5.png"),pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan6.png"), pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan7.png"), pygame.image.load("./Assets/Img/Pemain/Kanan/Kanan8.png")]

    def __init__(self):
        pass

    def pergerakan(self, screen):
        if self.gerak_count >= 21:
            self.gerak_count = 0

        if self.gerak_kiri == True:
            self.pemain_x += self.kecepatan_x
            self.gerak_count += 1
            screen.blit(self.animasi_kiri[self.gerak_count // 3], (self.pemain_x, self.pemain_y))
        elif self.gerak_kanan == True:
            self.pemain_x += self.kecepatan_x
            self.gerak_count += 1
            screen.blit(self.animasi_kanan[self.gerak_count // 3], (self.pemain_x, self.pemain_y))
        else:
            self.gerak_count = 0
            screen.blit(self.animasi_diam, (self.pemain_x, self.pemain_y))

    def isTouch(self, x, y):
        distance = math.sqrt(math.pow(self.pemain_x - x, 2) + (math.pow(self.pemain_y - y, 2)))
        if distance < 22:
            return True
        else:
            return False
        
    def isAbleToInteract(self, x, y):
        distance = math.sqrt(math.pow(self.pemain_x - x, 2) + (math.pow(self.pemain_y - y, 2)))
        if distance < 27:
            return True
        else:
            return False
