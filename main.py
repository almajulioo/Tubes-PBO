import pygame
from Object.Pemain import Pemain
from Object.Peti import Peti
from pygame.locals import *

# Inisialisasi Pygame
pygame.init()

# Membuat dan mengatur ukuran windows
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Judul
pygame.display.set_caption("Maze Game")

# Pemain
pemain = Pemain()

# Peti
peti = Peti()

running = True
while running:
     clock.tick(30)
     screen.fill((0, 0, 0))
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_a:
                    pemain.kecepatan_x = -3
                    pemain.gerak_kiri = True
               if event.key == pygame.K_d:
                    pemain.kecepatan_x = 3
                    pemain.gerak_kanan = True
               if event.key == pygame.K_f and pemain.isAbleToInteract(peti.peti_x, peti.peti_y):
                    peti.buka = True
          if event.type == pygame.KEYUP:
               if event.key == pygame.K_a:
                    pemain.gerak_kiri = False
                    pemain.animasi_diam = pemain.animasi_kiri[0]
               if event.key == pygame.K_d:
                    pemain.gerak_kanan = False
                    pemain.animasi_diam = pemain.animasi_kanan[0]
               
     if pemain.isTouch(peti.peti_x, peti.peti_y):
          pemain.pemain_x -= pemain.kecepatan_x
     
     pemain.pergerakan(screen)
     peti.pergerakan(screen)
     pygame.display.update()