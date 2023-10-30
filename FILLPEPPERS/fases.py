import pygame
from pygame.locals import *
import info
import os
from sys import exit
import time
from personagens import Perso

class Fases():
    def __init__(self, tela):
        ###INFORMAÇÕES DA TELA
        self.tela = tela
        self.relogio = pygame.time.Clock()
        self.intervalo = pygame.time.get_ticks()
        

        #EFEITO PARALLAX CASO NECESSARIO
        self.scrol = 0
        self.num = 3
        self.bg_imagens = []
        direImagens = os.path.join(os.getcwd(), "imagens")
        for i in range(1,3):
            cenario = os.path.join(direImagens, f"cenario{i}.png")
            bg_imagem = pygame.image.load(cenario).convert_alpha()
            self.bg_imagens.append(bg_imagem)
            
        self.bg_width = self.bg_imagens[0].get_width()

        #######PERSONAGENS
        self.personagem = Perso(self.tela)
        self.persoInimigo = Perso(self.tela)
        self.tiro = Perso(self.tela)
        self.mascara_personagem = None
        self.mascara_persoInimigo = None
        ##TIRO
        self.tiros = []
        self.tecla_controle_disparo = 0
        
    
    

    def fase1(self):
        jogando = True
        colidiu = False
        pulando = False
        tiro_visivel = False

        
        self.personagem.criarPersonagem("nave.png")
        self.persoInimigo.criarPersonagem("naveInimigo.png")
        self.tiro.criarPersonagem("shoot.png")
        

        while jogando:
            self.relogio.tick(info.FPS) 
            self.tela.fill((73, 81, 82))
            
            #CENARIO 
            self.cenario()
            # personagem = pygame.draw.rect(self.tela,info.VERMELHO,(info.X_PERSONAGEM + 10, info.Y_PERSONAGEM + 3, 88,90))
            self.personagem.mostrarPersonagem(info.X_PERSONAGEM, info.Y_PERSONAGEM)
            self.persoInimigo.mostrarPersonagem(info.X_PERSOINIMIGO,info.Y_PERSOINIMIGO)
            

            if self.mascara_personagem is None:
                self.mascara_personagem = pygame.mask.from_surface(self.personagem.personagens)
            if self.mascara_persoInimigo is None:
                self.mascara_persoInimigo = pygame.mask.from_surface(self.persoInimigo.personagens)

            if self.mascara_personagem.overlap(self.mascara_persoInimigo,(info.X_PERSOINIMIGO - info.X_PERSONAGEM, info.Y_PERSOINIMIGO - info.Y_PERSONAGEM)):
                print("Colidiu")


            for evento in pygame.event.get():
                if evento.type == QUIT:
                    jogando = False
                    pygame.quit()
                    exit()   

                if evento.type == KEYUP:
                    if tecla[pygame.K_SPACE]:
                        self.dispararTiro() 
            
            
            tecla = pygame.key.get_pressed()
            tempoAtual = pygame.time.get_ticks()
            ######################################
            #Atualiza a posição do objeto com base nas teclas pressionadas
            if tecla[pygame.K_d]:
                info.X += info.VELOCIDADE
                info.X_PERSONAGEM += info.VELOCIDADE
                
            if tecla[pygame.K_a]:
                info.X -= info.VELOCIDADE
                info.X_PERSONAGEM -= info.VELOCIDADE

            if tecla[pygame.K_w]:
                info.Y -= info.VELOCIDADE
                info.Y_PERSONAGEM -= info.VELOCIDADE

            if tecla[pygame.K_s]:
                info.Y += info.VELOCIDADE
                info.Y_PERSONAGEM += info.VELOCIDADE

                    
                      

            if tecla[pygame.K_RIGHT]:
                info.X += info.VELOCIDADE
                info.X_PERSOINIMIGO += info.VELOCIDADE

            if tecla[pygame.K_LEFT]:
                info.X -= info.VELOCIDADE
                info.X_PERSOINIMIGO -= info.VELOCIDADE

            if tecla[pygame.K_UP]:
                info.Y -= info.VELOCIDADE
                info.Y_PERSOINIMIGO -= info.VELOCIDADE

            if tecla[pygame.K_DOWN]:
                info.Y += info.VELOCIDADE
                info.Y_PERSOINIMIGO += info.VELOCIDADE        
                
            #######################################     
            
            
            self.atualizar()

            ###############################
            #SISTEMA DE COLISÃO

            # if not colidiu:
            #     info.VELOY += info.GRAVIDADE
            #     info.Y += info.VELOY
                    
            #     if info.Y + 70 > 720:
            #         colidiu = True
            #         info.Y = 720 - 70
            #         info.VELOY = 0
            #         pulando = False      
                
            #     elif info.Y + 70 < 0:
            #         colidiu = True
            #         info.Y = 720 + 70
            #         # info.VELOY = 0
            #         pulando = False

            #     if info.X + 70 > 1280:
            #         print("colidu")
            colidiu = False
            ###################################
            self.tecla_controle_disparo = False
            ########################################
            #PASSAGEM DAS IMAGENS
            self.scrol += 5
            
            controleTempo = pygame.time.get_ticks()
            
            if controleTempo - self.intervalo >= 5000:
                self.num += 1
                self.intervalo = controleTempo
            ############################################
            
            pygame.display.update()
    
    ###CONFIGURAÇÕES DO TIRO
    def dispararTiro(self):
        xTiro = info.X_PERSOINIMIGO - 40
        yTiro = info.Y_PERSOINIMIGO + 10
        tiro_visivel = True
        tiroX = xTiro
        tiroY = yTiro
        # info.VELOY = -info.PULO
        # pulando = True
        if tiro_visivel:
            tiroX -= info.VELOTIRO
            self.tiro.mostrarPersonagem(tiroX, yTiro)
            print(tiroX)
            if tiroX < -50:
                print("OK")
                tiro_visivel = False
            self.tiros.append({"x": tiroX, "y": yTiro})
                

    def atualizar(self):
        for tiro in self.tiros:
            tiro["x"] -= info.VELOTIRO
            self.tiro.mostrarPersonagem(tiro["x"], tiro["y"])
    #EFEITO PARALLAX CASO NECESSARIO
    def cenario(self):
        for x in range(self.num):
            for e in self.bg_imagens:
                self.tela.blit(e,((x * self.bg_width) - self.scrol,0)) 

            
        