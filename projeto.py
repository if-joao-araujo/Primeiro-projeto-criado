
import pygame
from time import sleep
def ultima_fase(): 
#para iniciar ,_,
    pygame.init()
    relogio = pygame.time.Clock()
    #minha janela             
    janela2 = pygame.display.set_mode([0,0], pygame.FULLSCREEN)
#minhas cores
    cor_branco = (225, 225, 225)
    cor_azul = (108, 194, 235)
    cor_amarelo = (252,240,0)
    cor_vermelho = (255,0,0)
    cor_roxa = (100,72,255)
    cor_preta = (0,0,0)
    cor_rosa = (255,52,194)
    sair = False
#som
    som_colisao = pygame.mixer.Sound('C:/Users/PC/OneDrive/Desktop/criação de jogos/smw_fireball.wav')
    som_fim = pygame.mixer.Sound('C:/Users/PC/OneDrive/Desktop/criação de jogos/smw_pipe.wav')
#meus objetos
    quadrado2 = pygame.Rect(1330,730,22,22)
    barreira1 = pygame.Rect(610,673,600,60)
    barreira2 = pygame.Rect(1280,700,40,90)
    barreira3 = pygame.Rect(375,550,900,29.5)
    barreira4 = pygame.Rect(10,495,1305,20)
    barreira5 = pygame.Rect(600,430,750,30) 
    barreira6 = pygame.Rect(562,370,750,20)
    barreira7 = pygame.Rect(458,300,1200,20)
    barreira8 = pygame.Rect(29,450,450,18)
    barreira9 = pygame.Rect(10,402,248,20)
    barreira10 = pygame.Rect(210,314,120,20)
    barreira11 = pygame.Rect(0,50,580,20)
    barreira12 = pygame.Rect(205,218,410,20)
    barreira13 = pygame.Rect(1042, 138,290,20)
    barreira14 = pygame.Rect(1058, 10,280,20)
    
    obstaculo1 = pygame.Rect(1200,640,150,15)
    obstaculo2 = pygame.Rect(450,620,110,140)
    obstaculo3 =pygame.Rect(560,620,595,15)
    obstaculo4 = pygame.Rect(1200,550,400,70)
    obstaculo5 = pygame.Rect(380,580,22,150)
    obstaculo6 = pygame.Rect(50,560,340,170)
    obstaculo7 = pygame.Rect(540,350,20,150)
    obstaculo8 = pygame.Rect(450,322,50,135)
    obstaculo9 = pygame.Rect(288,314,180,140)
    obstaculo10 = pygame.Rect(194,314,20,90)
    obstaculo11 = pygame.Rect(642,0,400,280)
    obstaculo12 = pygame.Rect(58,114,800,90)
    obstaculo13 = pygame.Rect(205,218,20,90)
    obstaculo14 = pygame.Rect(1090,170,30,125)
    obstaculo15 = pygame.Rect(1330, 26,10,110)


#final 
    fim1 = pygame.Rect(472,466,25,25)
    fim2 = pygame.Rect(248,358,10,10)
    fim3 = pygame.Rect(2,368,30,30)
    fim_fase =  pygame.Rect(1298,114,20,20)
   
#posição do meu quadrao2
    (quadrado2.x,quadrado2.y) = (1330,730)
    
    sair = False
    while sair == False:  
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
               sair = True  

        print(quadrado2)
      #movimentação do quadrado2  
        teclas2 = pygame.key.get_pressed()
        if teclas2[pygame.K_w]:
           quadrado2.y -= 8
        if  teclas2[pygame.K_s]:
            quadrado2.y += 8
        if teclas2[pygame.K_a]:
            quadrado2.x -= 8
        if teclas2[pygame.K_d]:
           quadrado2.x += 8 
    
        paredes = [barreira1, barreira2, barreira3, barreira4, barreira5,
                    barreira6, barreira7, obstaculo1, obstaculo2, obstaculo3,
                    obstaculo4, obstaculo5, obstaculo6, obstaculo7, obstaculo8]
        for colisao in paredes:
            if quadrado2.colliderect(colisao):
                (quadrado2.x, quadrado2.y) = (1330, 730)
                som_colisao.play()
                sleep(0.2)     
             
#colisão com os finais
        if quadrado2.colliderect(fim1):
           quadrado2.width = 10  
           quadrado2.height = 10  
           (quadrado2.x,quadrado2.y) = (434,466)
           som_fim.play()
           sleep(0.2)
        if quadrado2.colliderect(fim2):
            quadrado2.width = 30
            quadrado2.height = 30
            (quadrado2.x,quadrado2.y) = (10,10)
            som_fim.play()
            sleep(0.2) 
        if quadrado2.colliderect(fim3):
            quadrado2.width = 5
            quadrado2.height = 5
            
        if quadrado2.colliderect(fim_fase):
           sleep(5)
           return 
        
#objetos e as  telas que serão desenhados na janela2
        janela2.fill(cor_preta)
        pygame.draw.rect(janela2, cor_branco,quadrado2)
        pygame.draw.rect(janela2,cor_vermelho,barreira1)
        pygame.draw.rect(janela2,cor_vermelho,barreira2)
        pygame.draw.rect(janela2,cor_rosa,barreira3)  
        pygame.draw.rect(janela2,cor_vermelho,barreira4)
        pygame.draw.rect(janela2,cor_vermelho,barreira5)
        pygame.draw.rect(janela2,cor_rosa,barreira6)
        pygame.draw.rect(janela2,cor_vermelho,barreira7)
        pygame.draw.rect(janela2,cor_vermelho,barreira8)
        pygame.draw.rect(janela2,cor_vermelho,barreira9)
        pygame.draw.rect(janela2,cor_vermelho,barreira10)
        pygame.draw.rect(janela2,cor_vermelho,barreira11)
        pygame.draw.rect(janela2,cor_vermelho,barreira12)
        pygame.draw.rect(janela2,cor_vermelho,barreira13)
        pygame.draw.rect(janela2,cor_vermelho,barreira14)

        pygame.draw.rect(janela2,cor_rosa,obstaculo1)
        pygame.draw.rect(janela2,cor_rosa,obstaculo2)
        pygame.draw.rect(janela2,cor_rosa,obstaculo3)
        pygame.draw.rect(janela2,cor_rosa,obstaculo4)
        pygame.draw.rect(janela2,cor_rosa,obstaculo5)
        pygame.draw.rect(janela2,cor_rosa,obstaculo6)
        pygame.draw.rect(janela2,cor_rosa,obstaculo7)
        pygame.draw.rect(janela2,cor_rosa,obstaculo8)
        pygame.draw.rect(janela2,cor_rosa,obstaculo9)
        pygame.draw.rect(janela2,cor_rosa,obstaculo10)
        pygame.draw.rect(janela2,cor_rosa,obstaculo11) 
        pygame.draw.rect(janela2,cor_rosa,obstaculo12) 
        pygame.draw.rect(janela2,cor_rosa,obstaculo13)
        pygame.draw.rect(janela2,cor_rosa,obstaculo14)
        pygame.draw.rect(janela2,cor_rosa,obstaculo15)  
        
        pygame.draw.rect(janela2,cor_amarelo,fim1)
        pygame.draw.rect(janela2,cor_amarelo,fim2)
        pygame.draw.rect(janela2,cor_amarelo,fim3)
        pygame.draw.rect(janela2,cor_amarelo,fim_fase)
        
        relogio.tick(30)#FRAMES
        pygame.display.update()
    pygame.quit()  



def main():
    pygame.init()
    
    relogio = pygame.time.Clock()
    janela = pygame.display.set_mode([1300, 400]) #minha janela
    pygame.display.set_caption('Não encoste nas paredes') 
    
    # cores
    cor_branco = (225, 225, 225)
    cor_azul = (108, 194, 235)
    cor_amarelo = (252,240,0)
    cor_vermelho = (255,0,0)
    cor_roxa = (100,72,255)
    cor_preta = (0,0,0)
    cor_rosa = (255,52,194)
  
    
    #quadrado e os obstaculos
    quadrado = pygame.Rect(1,18,20,16)
    retangulo = pygame.Rect(0,35,1100,20)
    retangulo2 = pygame.Rect(50,80,1180,20)
    retangulo3 = pygame.Rect(0,130,700,20)
    retangulo4 = pygame.Rect(0,240,532,20)
    retangulo5 = pygame.Rect(600,180,700,20)
    retangulo6 = pygame.Rect(0,260,1170,40)
    retangulo7 = pygame.Rect(600,340,700,26)
    retangulo8 = pygame.Rect(50,340,580,26)

    retangulo_lateral = pygame.Rect(1140,0,110,90)
    retangulo_lateral2 = pygame.Rect(584,181,45,36)
    retangulo9 = pygame.Rect(50,190,529,15)
 
    fim = pygame.Rect(1170,370,30,30)
    
    #posição do quadrado no eixo x
    quadrado.y = 10
    quadrado.x = 10
   
    sair = False
    som_colisao = pygame.mixer.Sound('C:/Users/PC/OneDrive/Desktop/criação de jogos/smw_stomp.wav')
    
    while not sair:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:  
                sair = True
#MOVIMENTAÇÃO DO QUADRADO
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_w]:
               quadrado.y -= 10
        if  teclas[pygame.K_s]:
               quadrado.y += 10

        if teclas[pygame.K_a]:
               quadrado.x -= 10
        if teclas[pygame.K_d]:
                quadrado.x += 10     
          
#COLISÃO DO QUADRADO
        barreiras  = [retangulo,retangulo2,retangulo3,retangulo4,retangulo5,
                   retangulo6,retangulo7,retangulo_lateral,retangulo_lateral2,
                    retangulo9]
        for colisao in barreiras:
           if quadrado.colliderect(colisao):
              quadrado.x = 10
              quadrado.y = 10  
              som_colisao.play()
              sleep(0.5)
            
#Limite para não sair da tela pelo eixo x
        if quadrado.x <10 or quadrado.x >1300:
           quadrado.y = 10 
           quadrado.x = 10
           sleep(0.5)
#limite para não sair pelo eixo y
        if quadrado.y <10 or quadrado.y > 400:
           quadrado.y = 10
           quadrado.x = 10
           sleep(0.5)
      
        janela.fill(cor_preta)  # pinta a janela
        pygame.draw.rect(janela, cor_branco,quadrado ) 
        pygame.draw.rect(janela,cor_roxa,retangulo )
        pygame.draw.rect(janela,cor_roxa,retangulo2)
        pygame.draw.rect(janela,cor_roxa,retangulo3)
        pygame.draw.rect(janela,cor_roxa,retangulo4)
        pygame.draw.rect(janela,cor_roxa,retangulo5)
        pygame.draw.rect(janela,cor_roxa,retangulo6)
        pygame.draw.rect(janela,cor_roxa,retangulo7)
        pygame.draw.rect(janela,cor_roxa,retangulo8)
        pygame.draw.rect(janela,cor_vermelho,retangulo_lateral)
        pygame.draw.rect(janela,cor_vermelho,retangulo_lateral2)
        pygame.draw.rect(janela,cor_roxa,retangulo9)
        pygame.draw.rect(janela,cor_amarelo,fim)
        
       
        if quadrado.colliderect(fim):
           (quadrado.x , quadrado.y) = (1170, 370) 
           som_colisao.play()
           ultima_fase()
           break
        
        relogio.tick(30)#FRAMES POS SEGUNDO 
        pygame.display.update()
    pygame.quit()  
    

main()