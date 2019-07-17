import sys, pygame
from pygame.locals import *
from random import randint

SCREEN_WIDTH = 620
SCREEN_HEIGHT = 480
ICON_SIZE = 32

class nave(pygame.sprite.Sprite):
    def __init__(self):
        self.ImagenNave = pygame.image.load('Imagenes/rocket.png')
        self.rect = self.ImagenNave.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.centery = SCREEN_HEIGHT-30
        self.listaDisparo = []
        self.vida = 100
        self.velocidad = 20

    def movimiento(self):
        if self.vida == True:
            if self.rect.left <=0:
                self.rect.left =0
            elif self.rect.right>640:
                self.rect.right = 620 
    def disparar(self, x, y):
        bala = Bala(x,y,'Imagenes/bullet.png',True)
        self.listaDisparo.append(bala)
    def dibujar(self, superficie):
        superficie.blit(self.ImagenNave, self.rect)

class malo(pygame.sprite.Sprite):
    def __init__(self):
        self.ImagenMalo = pygame.image.load('Imagenes/spaceship.png')
        self.rect = self.ImagenMalo.get_rect()
        self.rect.centerx = 10
        self.rect.centery = 10
        self.listaDisparo = []
        self.vida = 100
        self.velocidad = 20

    def movimiento(self):
        if self.vida == True:
            if self.rect.left <=0:
                self.rect.left =0
            elif self.rect.right>640:
                self.rect.right = 620 
    def disparar(self, x, y):
        bala = Bala(x,y,'Imagenes/favorite.png',False)
        self.listaDisparo.append(bala)
    def dibujar(self, superficie):
        superficie.blit(self.ImagenMalo, self.rect)

class Bala(pygame.sprite.Sprite):
    def __init__(self, posx, posy,ruta, pers ):
        pygame.sprite.Sprite.__init__(self)

        self.imageBala = pygame.image.load(ruta)
        self.rect = self.imageBala.get_rect()
        self.velocidadDisparo = 10
        self.rect.top = posy
        self.rect.left = posx 
        self.disparoPersonaje = pers  
    def trayectoria(self):
        if self.disparoPersonaje == True:         
            self.rect.top = self.rect.top - self.velocidadDisparo
        else:
            self.rect.top = self.rect.top + self.velocidadDisparo
    def dibujar(self, superficie):
        superficie.blit(self.imageBala, self.rect)
                                            


def game():
      pygame.init()
      pygame.mixer.init()
      screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
      jugando = True
      pygame.display.set_caption("Galaxy" )
      fuente = pygame.font.Font(None, 30)
      background_image = pygame.image.load('Imagenes/fondo.jpg');
      pygame.mixer.music.load('Sonidos/intro.mp3')
      pygame.mixer.music.play()
      pygame.mouse.set_visible( False )
      temporizador = pygame.time.Clock()

      NAVE = nave()
      MALO = malo()
      while jugando:

          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  sys.exit()

              if event.type == pygame.KEYDOWN:
                  if event.key == K_LEFT:
                      NAVE.rect.left -= NAVE.velocidad
                  elif event.key == K_RIGHT:
                      NAVE.rect.right += NAVE.velocidad
                  elif event.key == K_UP:
                      x,y= NAVE.rect.center
                      NAVE.disparar(x,y)
             
                  if event.key == K_a:
                      MALO.rect.left -= MALO.velocidad
                  elif event.key == K_d:
                      MALO.rect.right += MALO.velocidad
                  elif event.key == K_w:
                      x,y= MALO.rect.center
                      MALO.disparar(x,y)
                      
          screen.blit(background_image, (0,0))  
          NAVE.dibujar(screen)
          MALO.dibujar(screen)
          Fuente = pygame.font.SysFont("Arial",30)
          if NAVE.vida<=0:
              jugando= False
              Texto = Fuente.render("Fin del juego gano la nave 2", 1,(250,250,250))
              pygame.mixer.music.fadeout(3000)
          if len(NAVE.listaDisparo)>0:
              for x in NAVE.listaDisparo:
                  x.dibujar(screen)
                  x.trayectoria()
          for x in NAVE.listaDisparo:
              if MALO.rect.colliderect(x.rect):
                  MALO.vida-= 2
          if MALO.vida<=0:       
               jugando= False
               Texto = Fuente.render("Fin del juego gano la nave 1", 1,(250,250,250))
               pygame.mixer.music.fadeout(3000)
                  
          if len(MALO.listaDisparo)>0:
              for x in MALO.listaDisparo:
                  x.dibujar(screen)
                  x.trayectoria()
          for x in MALO.listaDisparo:
              if NAVE.rect.colliderect(x.rect):
                  NAVE.vida-= 2
          texto_vida = fuente.render("Vida: "+str(MALO.vida), 1, (250,250,250))
          screen.blit(texto_vida, (10,100))
          pygame.display.update()       
          texto_vida = fuente.render("Vida: "+str(NAVE.vida), 1, (250,250,250))
          screen.blit(texto_vida, (10,300))
          

          if jugando == False:
              screen.blit(Texto,(250,250))
          pygame.display.update()

game()
