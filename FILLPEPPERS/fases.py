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
        
    def fase1(self):
        jogando = True
        colidiu = False
        pulando = False
        controle = 0
        

        while jogando:
            self.relogio.tick(info.FPS) 
            self.tela.fill((73, 81, 82))
            #CENARIO 
            self.cenario()

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    jogando = False
                    pygame.quit()
                    exit()   

            tecla = pygame.key.get_pressed()
            
            
            ######################################
            #Atualiza a posição do objeto com base nas teclas pressionadas
            if tecla[pygame.K_d]:
                # self.scrol = 0
                
                 
                info.X += info.VELOCIDADE
                
            
            if tecla[pygame.K_a]:
                 
                info.X -= info.VELOCIDADE

            if tecla[pygame.K_SPACE] and not pulando:
                info.VELOY = -info.PULO
                pulando = True
                
            #######################################     
            
            personagem = pygame.draw.rect(self.tela,info.VERMELHO,(info.X, info.Y, 70,70))

            ###############################
            #SISTEMA DE COLISÃO
            


            if not colidiu:
                info.VELOY += info.GRAVIDADE
                info.Y += info.VELOY
                    
                if info.Y + 70 > 720:
                    colidiu = True
                    info.Y = 720 - 70
                    info.VELOY = 0
                    pulando = False      
                
                elif info.Y + 70 < 0:
                    colidiu = True
                    info.Y = 720 + 70
                    # info.VELOY = 0
                    pulando = False

                if info.X + 70 > 1280:
                    print("colidu")
            colidiu = False
            ###################################

            self.scrol += 5
            controle += 6

            if controle > 2500:
                controle = 0
            print("SCROL: ", self.scrol)
            print("CONTROLE: ", controle)

            if self.scrol > controle:
                self.num += 1
                print("NUM: ", self.num)
                break
            
            
            # pygame.draw.polygon(self.tela, info.BRANCO, [(100, 100), (200, 100), (150, 200)])
           
            pygame.display.update()


    #EFEITO PARALLAX CASO NECESSARIO
    def cenario(self):
        for x in range(self.num):
            
            for e in self.bg_imagens:
                self.tela.blit(e,((x * self.bg_width) - self.scrol,0)) 

            
    
    
    # def cenarioParede(self):
        
                


            

            
