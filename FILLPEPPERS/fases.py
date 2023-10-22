import pygame
from pygame.locals import *
import info
import os
from sys import exit
import time

class Fases():
    def __init__(self, tela):
        
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
        self.personagens = None
        
    
    def moviPersonagem(self):
        self.tela.blit(self.personagens, (info.X_PERSONAGEM,info.Y_PERSONAGEM))

    def fase1(self):
        jogando = True
        colidiu = False
        pulando = False
        
        direImagem = os.path.join(os.getcwd(), "imagens")
        self.personagens = os.path.join(direImagem, "nave.png")
        self.personagens = pygame.image.load(self.personagens).convert_alpha()

        while jogando:
            self.relogio.tick(info.FPS) 
            self.tela.fill((73, 81, 82))
            
            #CENARIO 
            self.cenario()
            personagem = pygame.draw.rect(self.tela,info.VERMELHO,(info.X_PERSONAGEM + 10, info.Y_PERSONAGEM + 3, 88,90))
            self.moviPersonagem()

            perso = pygame.draw.rect(self.tela, (0,0,255), (200,200,90,90))


            if personagem.colliderect(perso):
                print("colidiu")


            for evento in pygame.event.get():
                if evento.type == QUIT:
                    jogando = False
                    pygame.quit()
                    exit()   

            tecla = pygame.key.get_pressed()
            
            
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

            if tecla[pygame.K_SPACE] and not pulando:
                info.VELOY = -info.PULO
                pulando = True
                
            #######################################     
            
            

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

            ########################################
            #PASSAGEM DAS IMAGENS
            self.scrol += 5
            
            controleTempo = pygame.time.get_ticks()
            
            if controleTempo - self.intervalo >= 5000:
                self.num += 1
                self.intervalo = controleTempo
            ############################################
            
            pygame.display.update()


    #EFEITO PARALLAX CASO NECESSARIO
    def cenario(self):
        for x in range(self.num):
            for e in self.bg_imagens:
                self.tela.blit(e,((x * self.bg_width) - self.scrol,0)) 

            
        