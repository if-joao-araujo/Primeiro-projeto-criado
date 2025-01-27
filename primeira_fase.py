import pygame
from time import sleep
def fase_inicial():
    pygame.init()
    relogio = pygame.time.Clock()
    telinha = pygame.display.set_mode([400,400])

    #cores
    cor_branco = (225, 225, 225)
    cor_azul = (108, 194, 235)
    cor_amarelo = (252,240,0)
    cor_vermelho = (255,0,0)
    cor_roxa = (100,72,255)
    cor_preta = (0,0,0)
    cor_rosa = (255,52,194)

    #objetos
    quadrado = pygame.Rect(10,10,20,20)
    parede1 = pygame.Rect(0,30,360,40)
    parede2 = pygame.Rect(30,110,360,40)
    parede3 = pygame.Rect(30,150,40,100)
    parede4 = pygame.Rect(0,290,120,50)
    parede5 = pygame.Rect(100, 180,20,110)
    parede6 = pygame.Rect(100, 175,240,20)
    parede7 = pygame.Rect(340,175,20,177)
    parede8 = pygame.Rect(0,340,365,30)

    #final da fase
    fim =  pygame.Rect(10,370,30,30)
    #posição quadrado
    quadrado.y = 10
    quadrado.x = 10
    som_colisao = pygame.mixer.Sound('C:/Users/PC/OneDrive/Documentos/Projeto_ip_privado/projeto_ip_privado/smw_fireball.wav')
    sair = False
    while sair == False:
       for evento in pygame.event.get():
           if evento.type == pygame.QUIT:
              sair = True
       movimentação = pygame.key.get_pressed()
       if movimentação[pygame.K_w]:
          quadrado.y -=10 
       if movimentação[pygame.K_s]: 
          quadrado.y +=10
       if movimentação[pygame.K_a]:
          quadrado.x -=10
       if movimentação[pygame.K_d]:
          quadrado.x +=10
       print(quadrado)
#colisoes 
       obstaculos = [parede1,parede2,parede3,parede4,parede5,parede6,
                     parede7,parede8]
       for colisao in obstaculos:
           if quadrado.colliderect(colisao):
              som_colisao.play()
              sleep(0.5)
              quadrado.x = 10
              quadrado.y = 10 
 #colisão com final
       if quadrado.x <0 or quadrado.x>400:
          sleep(0.5)
          quadrado.x = 10
          quadrado.y = 10
       if quadrado.y < 5 or quadrado.y >400:
          sleep(0.5)
          quadrado.y = 10
          quadrado.x = 10
       if quadrado.colliderect(fim):
          sleep(2)
          break
       telinha.fill(cor_branco)
       pygame.draw.rect(telinha,cor_azul,quadrado)
       pygame.draw.rect(telinha,cor_preta,parede1)
       pygame.draw.rect(telinha,cor_preta,parede2)
       pygame.draw.rect(telinha,cor_preta,parede3)
       pygame.draw.rect(telinha,cor_preta,parede4)
       pygame.draw.rect(telinha,cor_preta,parede5)
       pygame.draw.rect(telinha,cor_preta,parede6)
       pygame.draw.rect(telinha,cor_preta,parede7)
       pygame.draw.rect(telinha,cor_preta,parede8)

       pygame.draw.rect(telinha,cor_amarelo,fim)
       relogio.tick(30)
       pygame.display.update()
    pygame.quit()

fase_inicial()