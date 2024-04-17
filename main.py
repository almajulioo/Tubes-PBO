import pygame
from pygame.locals import *
# Inisialisasi Pygame
pygame.init()

# Membuat dan mengatur ukuran windows
screen = pygame.display.set_mode((800, 600), RESIZABLE)

# Judul
pygame.display.set_caption("Tower Defense")

# Load background
background = pygame.image.load("./Assets/img/grass_bg.jpg")
screen.blit(pygame.transform.scale(background, (800, 600)), (0,0))

running = True
while running:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               running = False
          elif event.type == VIDEORESIZE:
               screen = pygame.display.set_mode(event.dict['size'], RESIZABLE)
               screen.blit(pygame.transform.scale(background, event.dict['size']), (0,0))
               pygame.display.flip()

     pygame.display.update()