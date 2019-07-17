import sys, pygame
from pygame.locals import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
ICON_SIZE = 32

class nave(pygame.sprite.Sprite):
    def __init__(self):
        self.ImagenNave = pygame.image.load('Imagenes/nave.jpg')
        self.rect = self.ImagenNave.get_rect()
        self.rect.centerx = ancho/2
        self.rect.centery = alto-30
        self.listaDisparo = []
        self.vida = True

    def disparar(self):
        pass

    def dibujar(self, superficie):
        superficie.blit(self.ImagenNave, self.rect)
        


def game():
      pygame.init()
      pygame.mixer.init()
      screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
      jugando = True
      pygame.display.set_caption("Galaxy" )
      fuente = pygame.font.Font(None, 30)
      background_image = UTIL.cargar_imagen('Imagenes/fondo.jpg');

      NAVE = nave()

      while jugando:          
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  sys.exit()
          NAVE.dibujar(screen)
          pygame.display.update()
