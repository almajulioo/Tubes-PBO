try:
     import pygame
except:
     print("Anda belum menginstall pygame!")

from Object.Pemain import Pemain
from Object.Peti import semua_peti
from Object.Dinding import semua_dinding
from Object.Background import semua_background
from Object.Maps import Maps
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

# Maps
maps = Maps()

running = True
while running:
     # Setting Frame Per Second
     clock.tick(FPS)

     # Selalu Mengisi screen dengan layar hitam
     screen.fill((0, 0, 0))

     # Penanganan event pygame
     for event in pygame.event.get():
          # Penanganan jika ingin keluar
          if event.type == pygame.QUIT:
               running = False
          
          # Penanganan jika menekan suatu tombol
          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_a and pemain.gerak_kanan == False:
                    pemain.gerak_kiri = True
               if event.key == pygame.K_d and pemain.gerak_kiri == False:
                    pemain.gerak_kanan = True
               if event.key == pygame.K_w and pemain.gerak_bawah == False:
                    pemain.gerak_atas = True
               if event.key == pygame.K_s and pemain.gerak_atas == False:
                    pemain.gerak_bawah = True
               if event.key == pygame.K_f:
                    for peti in semua_peti.sprites():
                         if pemain.isAbleToInteract(peti.rect.topleft):
                              peti.buka = True
          
          # Penanganan jika melepas suatu tombol
          if event.type == pygame.KEYUP:
               if event.key == pygame.K_a:
                    pemain.gerak_kiri = False
                    pemain.animasi_diam = pemain.animasi_kiri[0]
               if event.key == pygame.K_d:
                    pemain.gerak_kanan = False
                    pemain.animasi_diam = pemain.animasi_kanan[0]
               if event.key == pygame.K_w:
                    pemain.gerak_atas = False
               if event.key == pygame.K_s:
                    pemain.gerak_bawah = False

     # Melakukan update untuk setiap objek (Berguna juga untuk mengatur layer dari yang terbelakang hingga terdepan)
     semua_background.update(screen)
     semua_dinding.update(screen)
     semua_peti.update(screen)
     pemain.update(screen)

     # Melakukan update setiap iterasi
     pygame.display.update()