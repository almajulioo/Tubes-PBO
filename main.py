import pygame
from pygame.locals import *
# Inisialisasi Pygame
pygame.init()

# Membuat dan mengatur ukuran windows
screen = pygame.display.set_mode((800, 600))

# Judul
pygame.display.set_caption("Maze Game")

running = True
while running:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
         

     pygame.display.update()