import pygame
import sys
import time
from Object.Pemain import Pemain
from Object.Kunci import semua_kunci
from Object.Peti import semua_peti
from Object.Dinding import semua_dinding
from Object.Background import semua_background
from Object.Maps import Maps
from Object.Button import Button
from pygame.locals import *



class Game:
     def __init__(self):
          pygame.init()

          pygame.display.set_caption("Maze Rusher")
          self.screen = pygame.display.set_mode((800, 600))
          self.display = pygame.Surface((400, 300))

          self.clock = pygame.time.Clock()

          self.pemain = Pemain()

          self.maps = Maps()

          self.scroll = [0,0]
          # pygame.mixer.music.load("./Assets/Music/background_music.mp3")
          # pygame.mixer.music.play(-1)
          
          self.timer_menit = 1
          self.timer_detik = 3 

          self.font = pygame.font.SysFont('Consolas', 30)
          pygame.time.set_timer(pygame.USEREVENT, 1000)
          
          self.game_over = False
          self.win = False

     def get_font(self, size): 
          return pygame.font.SysFont('Consolas', size)

     def menu(self):
            while True:
               bgmenu = pygame.image.load("./Assets/Img/Menu/bg_menu.png")
               self.screen.blit(bgmenu, (0, 0))

               menu_mouse_pos = pygame.mouse.get_pos()

               menu_text = self.get_font(50).render("MAIN MENU", True, "#b68f40")
               menu_rect = menu_text.get_rect(center=(400, 150))

               over_text = self.get_font(50).render("GAME OVER", True, "red")
               over_rect = menu_text.get_rect(center=(400, 150))

               win_text = self.get_font(50).render("YOU WIN", True, "green")
               win_rect = menu_text.get_rect(center=(425, 150))

               play_button = Button(image=pygame.image.load("./Assets/Img/Menu/Rect.png"), pos=(400, 250), 
                                   text_input="PLAY", font=self.get_font(45), base_color="#d7fcd4", hovering_color="White")
               quit_button = Button(image=pygame.image.load("./Assets/Img/Menu/Rect.png"), pos=(400, 400), 
                                   text_input="QUIT", font=self.get_font(35), base_color="#d7fcd4", hovering_color="White")

               
               if self.game_over == True:
                    self.screen.blit(over_text, over_rect)
               elif self.win == True:
                    self.screen.blit(win_text, win_rect)
               else:
                    self.screen.blit(menu_text, menu_rect)

               for button in [play_button,  quit_button]:
                    button.changeColor(menu_mouse_pos)
                    button.update(self.screen)
               
               for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                         pygame.quit()
                         sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                         if play_button.checkForInput(menu_mouse_pos):
                              self.game_over = False
                              self.win = False
                              self.run()
                         if quit_button.checkForInput(menu_mouse_pos):
                              pygame.quit()
                              sys.exit()

               pygame.display.update()

     def run(self):
          while True:
               # Setting Frame Per Second
               self.clock.tick(30)

               # Camera 
               self.scroll[0] += (self.pemain.rect[0] - self.display.get_width() / 2 - self.scroll[0])
               self.scroll[1] += (self.pemain.rect[1] - self.display.get_height() / 2 - self.scroll[1])
               
               # Selalu Mengisi screen dengan layar hitam
               self.display.fill((0, 0, 0))
               


               # Penanganan event pygame
               for event in pygame.event.get():
                    # Penanganan jika ingin keluar
                    if event.type == pygame.QUIT:
                         pygame.quit()
                         sys.exit()

                    if event.type == pygame.USEREVENT:
                         self.timer_detik -= 1
                         if self.timer_detik == -1:
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
               semua_background.update(self.display, self.scroll)
               semua_dinding.update(self.display, self.scroll)
               semua_peti.update(self.display, self.scroll)
               semua_kunci.update(self.display, self.scroll)
               self.pemain.update(self.display, self.scroll)
               
              
               self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
               if self.timer_detik <= 10:
                    self.screen.blit(self.font.render(f"0{self.timer_menit}:0{self.timer_detik}", True, (255, 255, 255)), (700, 50))
               else:
                    self.screen.blit(self.font.render(f"0{self.timer_menit}:{self.timer_detik}", True, (255, 255, 255)), (700, 50))

               self.screen.blit(self.font.render(f"Kunci Terambil : {self.pemain.kunci_terambil}", True, (255, 255, 255)), (20, 50))

               if self.timer_menit == 0 and self.timer_detik == 0:
                    self.game_over = True
                    self.menu()

               # Melakukan update setiap iterasi
               pygame.display.update()
               

Game().menu()