import pygame
from Object.Pemain import Pemain
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


running = True
while running:
     clock.tick(24)
     screen.fill((0, 0, 0))
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_a:
                    pemain.gerak_kiri = True
               if event.key == pygame.K_d:
                    pemain.gerak_kanan = True
          if event.type == pygame.KEYUP:
               if event.key == pygame.K_a:
                    pemain.gerak_kiri = False
                    pemain.animasi_diam = pemain.animasi_kiri[0]
               if event.key == pygame.K_d:
                    pemain.gerak_kanan = False
                    pemain.animasi_diam = pemain.animasi_kanan[0]
               
         
     pemain.Pergerakan(screen)
     pygame.display.update()