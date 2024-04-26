import pygame
from Object.Pemain import Pemain
from Object.Peti import Peti, semua_peti
from Object.Dinding import semua_dinding, Block
from pygame.locals import *

# Inisialisasi Pygame
pygame.init()

# Membuat dan mengatur ukuran windows
screen = pygame.display.set_mode((800, 600))

#FPS
clock = pygame.time.Clock()
FPS = 30

# Judul
pygame.display.set_caption("Maze Game")

# Pemain
pemain = Pemain()

# Peti
peti = Peti()

# Dinding
dinding = Block(50, 30)


running = True
while running:
     clock.tick(FPS)
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
               
     semua_dinding.update(screen)
     # semua_dinding.draw(screen)

     pemain.update(screen)
     peti.update(screen)
     pygame.display.update()