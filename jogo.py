import pygame
from random import randint

pygame.init();

class Carro:
  def __init__(self, imagem: str, x: int, y: int, velocidade: int, posicao:str):
    self.nome = imagem
    self.imagem = pygame.image.load(imagem)
    self.x = x
    self.y = y
    self.posicao= posicao
    self.velocidade = velocidade

janela = pygame.display.set_mode((1280,700))
carros = []

taxi = Carro('imagens/carro4.png', 400,1360,15, 'esquerda')
carros.append(taxi)

taxi = Carro('imagens/carro1.png', 400,1560,13, 'esquerda')
carros.append(taxi)

ambulancia = Carro('imagens/carro5.png', 760,1360,25, 'direita')
carros.append(ambulancia)

ambulancia = Carro('imagens/carro2.png', 760,1560,22, 'direita')
carros.append(ambulancia)

policia = Carro('imagens/carro3.png', 580,1360,27,'centro')
carros.append(policia)

policia = Carro('imagens/carro6.png', 580,1560,24,'centro')
carros.append(policia)

font = pygame.font.SysFont('Arial black', 60)
texto = font.render("Tempo: ",True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (105,70)

textoFim = font.render("GAME OVER",True,(255,0,0),(255,255,255))
textoFim2 = font.render("precione SPACE para continuar",True,(0,0,0),(255,255,255))
pos_textoFim = textoFim.get_rect()
pos_textoFim.center = (640,100)

pos_textoFim2 = textoFim2.get_rect()
pos_textoFim2.center = (640,160)

carroPrincipal = Carro('imagens/carroPrincipal.png', 640,100,20,'centro')
carros.append(carroPrincipal)

timer = 0
explosao=False
tempo_segundo = 0

fundo = pygame.image.load('imagens/fundo.png')
janela_aberta = True

#music

pygame.mixer.music.load("sons/Som ambiente trânsito na rodovia - Ambient Road Traffic.mp3")
pygame.mixer.music.set_volume(4)
pygame.mixer.music.play(-1)



pygame.display.set_caption('Trabalho Final de CGR')
while (janela_aberta):

    pygame.time.delay(50)

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if(comandos[pygame.K_UP]):
        carroPrincipal.y-=carroPrincipal.velocidade
    if(comandos[pygame.K_DOWN]):
        carroPrincipal.y+=carroPrincipal.velocidade
    if(comandos[pygame.K_RIGHT] and carroPrincipal.x < 800):
        carroPrincipal.x+=carroPrincipal.velocidade
    if(comandos[pygame.K_LEFT] and carroPrincipal.x >380):
        carroPrincipal.x-=carroPrincipal.velocidade

    if(comandos[pygame.K_SPACE] and explosao):
        carros = []

        taxi = Carro('imagens/carro4.png', 400,1360,15, 'esquerda')
        carros.append(taxi)

        taxi = Carro('imagens/carro1.png', 400,1560,13, 'esquerda')
        carros.append(taxi)

        ambulancia = Carro('imagens/carro5.png', 760,1360,25, 'direita')
        carros.append(ambulancia)

        ambulancia = Carro('imagens/carro2.png', 760,1560,22, 'direita')
        carros.append(ambulancia)

        policia = Carro('imagens/carro3.png', 580,1360,27,'centro')
        carros.append(policia)

        policia = Carro('imagens/carro6.png', 580,1560,24,'centro')
        carros.append(policia)

        carroPrincipal = Carro('imagens/carroPrincipal.png', 640,100,20,'centro')
        carros.append(carroPrincipal)

        timer = 0
        explosao=False
        tempo_segundo = 0

    janela.blit(fundo,(0,0))
    
    if(carroPrincipal.y>820):
        carroPrincipal.y = -100

    if(carroPrincipal.y<-100):
        carroPrincipal.y = 820

    if(timer < 20):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: "+str(tempo_segundo),True,(255,255,255),(0,0,0))
        timer = 0


    for carro in carros:
        if(carro.nome != "imagens/carroPrincipal.png"):
            carro.y-=carro.velocidade
            if(carro.y <= -200):
                if(carro.velocidade == 13 or carro.velocidade == 22 or carro.velocidade == 24):
                    carro.y=randint(1600,1800)
                else:
                    carro.y=randint(900,1300)
            


    ###########Colisao#############

    for carro in carros:
        if(carro.nome != "imagens/carroPrincipal.png"):
            if (carroPrincipal.x + 80 > carro.x and (carroPrincipal.y+150 >= carro.y >= carroPrincipal.y-150) and carro.posicao == 'direita'):
                explosao_imagem = pygame.image.load('imagens/crash.png')
                explosao_pos = (carroPrincipal.x-200, carroPrincipal.y)
                explosao=True
                carroPrincipal.x=5000

            elif (carroPrincipal.x - 80 < carro.x and (carroPrincipal.y+150 >= carro.y >= carroPrincipal.y-150) and carro.posicao == 'esquerda'):
                explosao_imagem = pygame.image.load('imagens/crash.png')
                explosao_pos = (carroPrincipal.x-200, carroPrincipal.y)
                explosao=True
                carroPrincipal.x=5000

            elif((carroPrincipal.x - 80 < carro.x < carroPrincipal.x + 80) and (carroPrincipal.y+150 >= carro.y >= carroPrincipal.y-150) and carro.posicao == 'centro'):
                explosao_imagem = pygame.image.load('imagens/crash.png')
                explosao_pos = (carroPrincipal.x-200, carroPrincipal.y)
                explosao=True
                carroPrincipal.x=5000
      

    ###############################

    for carro in carros:
        janela.blit(carro.imagem,(carro.x,carro.y))
    janela.blit(texto,pos_texto)

    if(explosao):
        janela.blit(explosao_imagem,explosao_pos)
        janela.blit(textoFim,pos_textoFim)
        janela.blit(textoFim2,pos_textoFim2)
        pygame.time.wait(150)

    pygame.display.update()

pygame.quit()    
