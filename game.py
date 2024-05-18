import pygame
import sys
from Object.Pemain import Pemain
from Object.Peti import semua_peti
from Object.Dinding import semua_dinding
from Object.Background import semua_background
from Object.Maps import Maps
from pygame.locals import *


class Game:
     def __init__(self):
          pygame.init()

          pygame.display.set_caption("Maze Rusher")
          self.screen = pygame.display.set_mode((800, 600))
          self.clock = pygame.time.Clock()

          self.pemain = Pemain()

          self.maps = Maps()

     def run(self):
          while True:
               # Setting Frame Per Second
               self.clock.tick(30)

               # Selalu Mengisi screen dengan layar hitam
               self.screen.fill((0, 0, 0))

               # Penanganan event pygame
               for event in pygame.event.get():
                    # Penanganan jika ingin keluar
                    if event.type == pygame.QUIT:
                         pygame.quit()
                         sys.exit()
                    
                    # Penanganan jika menekan suatu tombol
                    if event.type == pygame.KEYDOWN:
                         if event.key == pygame.K_a and self.pemain.gerak_kanan == False:
                              self.pemain.gerak_kiri = True
                         if event.key == pygame.K_d and self.pemain.gerak_kiri == False:
                              self.pemain.gerak_kanan = True
                         if event.key == pygame.K_w and self.pemain.gerak_bawah == False:
                              self.pemain.gerak_atas = True
                         if event.key == pygame.K_s and self.pemain.gerak_atas == False:
                              self.pemain.gerak_bawah = True
                         if event.key == pygame.K_f:
                              for peti in semua_peti.sprites():
                                   if self.pemain.isAbleToInteract(peti.rect.topleft):
                                        peti.buka = True
                    
                    # Penanganan jika melepas suatu tombol
                    if event.type == pygame.KEYUP:
                         if event.key == pygame.K_a:
                              self.pemain.gerak_kiri = False
                              self.pemain.animasi_diam = self.pemain.animasi_kiri[0]
                         if event.key == pygame.K_d:
                              self.pemain.gerak_kanan = False
                              self.pemain.animasi_diam = self.pemain.animasi_kanan[0]
                         if event.key == pygame.K_w:
                              self.pemain.gerak_atas = False
                         if event.key == pygame.K_s:
                              self.pemain.gerak_bawah = False

               # Melakukan update untuk setiap objek (Berguna juga untuk mengatur layer dari yang terbelakang hingga terdepan)
               semua_background.update(self.screen)
               semua_dinding.update(self.screen)
               semua_peti.update(self.screen)
               self.pemain.update(self.screen)

               # Melakukan update setiap iterasi
               pygame.display.update()

Game().run()