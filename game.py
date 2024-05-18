import pygame
import sys
import time
from Object.Pemain import Pemain
from Object.Kunci import semua_kunci
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

          self.fog = pygame.Surface((800, 600)).convert_alpha()
          
          self.timer_menit = 5
          self.timer_detik = 3 

          self.font = pygame.font.SysFont('Consolas', 30)
          pygame.time.set_timer(pygame.USEREVENT, 1000)
          

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

                    if event.type == pygame.USEREVENT:
                         self.timer_detik -= 1
                         if self.timer_detik == 0:
                              self.timer_menit -= 1
                              self.timer_detik = 59
                    
                    # Penanganan jika menekan suatu tombol
                    if event.type == pygame.KEYDOWN:
                         if event.key == pygame.K_a:
                              self.pemain.gerak_kiri = True
                         if event.key == pygame.K_d:
                              self.pemain.gerak_kanan = True
                         if event.key == pygame.K_w:
                              self.pemain.gerak_atas = True
                         if event.key == pygame.K_s:
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
               semua_kunci.update(self.screen)
               self.pemain.update(self.screen)

               self.fog.fill((7,7,10))
               pygame.draw.circle(self.fog, (0,0,0,50), self.pemain.rect.center, 50)
              
               self.screen.blit(self.fog, (0,0))

               if self.timer_detik <= 10:
                    self.screen.blit(self.font.render(f"0{self.timer_menit}:0{self.timer_detik}", True, (255, 255, 255)), (700, 50))
               else:
                    self.screen.blit(self.font.render(f"0{self.timer_menit}:{self.timer_detik}", True, (255, 255, 255)), (700, 50))


               # Melakukan update setiap iterasi
               pygame.display.update()
               

Game().run()