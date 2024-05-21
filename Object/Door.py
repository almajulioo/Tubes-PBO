import pygame

semua_door = pygame.sprite.Group()

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Door, self).__init__()
        self.door = pygame.image.load("./Assets/Img/Dinding/door.png")
        self.rect = self.door.convert_alpha().get_rect()
        self.sound = pygame.mixer.Sound("./Assets/Music/buka_pintu.mp3")
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        semua_door.add(self)
    
    def update(self, screen, offset):
        screen.blit(self.door, (self.rect[0] - offset[0], self.rect[1] - offset[1]))
        
    
  
    