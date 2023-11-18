import pygame
from pygame.locals import *
import info
import os
import random
from sys import exit
from personagens import Perso
from detalhes import Details

class Fases():
    def __init__(self, tela):
        ###----------INFORMAÇÕES DA TELA
        self.tela = tela
        self.relogio = pygame.time.Clock()
        self.intervalo = pygame.time.get_ticks()
        self.fonte = pygame.font.match_font(info.FONTE)
        self.detalhes = Details(tela)
        self.detalhes.carregarArquivos()

        #----------------EFEITO PARALLAX CASO NECESSARIO
        self.scrol = 0
        self.num = 3
        self.bg_imagens = []
        direImagens = os.path.join(os.getcwd(), "imagens")
        for i in range(1,3):
            cenario = os.path.join(direImagens, f"fundo{i}.png")
            bg_imagem = pygame.image.load(cenario).convert_alpha()
            self.bg_imagens.append(bg_imagem)
            
        self.bg_width = self.bg_imagens[0].get_width()
        self.controle = True
        #######-----------PERSONAGENS
        self.personagem = Perso(self.tela)
        self.tiro = Perso(self.tela)
        self.mascara_personagem = None
        self.mascaraTiroPersonagem = None
        self.mascaraTiroPersonagem = None
        ##---------INIMIGO
        self.direcao = "cima"
        self.persoInimigo = Perso(self.tela)
        self.mascara_persoInimigo = None
        self.mascaraTiroInimigo = None
        self.tempoMudanca = pygame.time.get_ticks() + random.randint(200,500)
        self.controle = pygame.time.get_ticks() + random.randint(500,1000)
        self.tiroInimigo = Perso(self.tela)
        self.tiroInimigo.xTiro = 0
        self.tiroInimigo.yTiro = 0
        self.mascaraTiroInimigo = None
    

    def fase1(self):
        jogando = True
       
        self.personagem.criarPersonagem("nave.png")
        self.persoInimigo.criarPersonagem("naveInimigo.png")
        self.tiro.criarPersonagem("laserf.png")
        self.tiroInimigo.criarPersonagem("lasern.png")

        pygame.mixer.music.load(os.path.join(self.detalhes.direSom, "raceAgaintSunset.mp3"))
        pygame.mixer.music.play()

        while jogando:
            self.relogio.tick(info.FPS) 
            self.tela.fill((73, 81, 82))
            
            
            #CENARIO 
            self.cenario()
            # personagem = pygame.draw.rect(self.tela,info.VERMELHO,(info.X_PERSONAGEM + 10, info.Y_PERSONAGEM + 3, 88,90))
            self.personagem.mostrarPersonagem(info.X_PERSONAGEM, info.Y_PERSONAGEM)
            self.persoInimigo.mostrarPersonagem(info.X_PERSOINIMIGO,info.Y_PERSOINIMIGO)
            
            self.mascara_personagem = pygame.mask.from_surface(self.personagem.personagens)
            self.mascara_persoInimigo = pygame.mask.from_surface(self.persoInimigo.personagens)
            tecla = pygame.key.get_pressed()

            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.mixer.music.stop()
                    jogando = False
                    pygame.quit()
                    exit()   

                if evento.type == KEYUP:
                    if tecla[pygame.K_SPACE]:
                        self.tiro.dispararTiro(info.X_PERSONAGEM, info.Y_PERSONAGEM, info.VELOTIRO,True)
                        pygame.mixer.Sound(os.path.join(self.detalhes.direSom, "disparo.mp3")).play()
                        
            
            
            
            tempoAtual = pygame.time.get_ticks()
            ######################################

            if tempoAtual >= self.tempoMudanca:
                self.direcao = random.choice(["cima", "baixo", "esquerda", "direita"])
                self.tempoMudanca = tempoAtual + random.randint(200,500)

            if tempoAtual >= self.controle:
                self.tiroInimigo.dispararTiro(info.X_PERSOINIMIGO, info.Y_PERSOINIMIGO, info.VELOTIRO,False) 
                pygame.mixer.Sound(os.path.join(self.detalhes.direSom, "disparo.mp3")).play()
                self.controle = tempoAtual + random.randint(1000,1500)  
                

            #Atualiza a posição do objeto com base nas teclas pressionadas
            if tecla[pygame.K_d] and info.X_PERSONAGEM < 1180:
                info.X += info.VELOCIDADE
                info.X_PERSONAGEM += info.VELOCIDADE
                
            if tecla[pygame.K_a] and info.X_PERSONAGEM > -17:
                info.X -= info.VELOCIDADE
                info.X_PERSONAGEM -= info.VELOCIDADE

            if tecla[pygame.K_w] and info.Y_PERSONAGEM > 0:
                info.Y -= info.VELOCIDADE
                info.Y_PERSONAGEM -= info.VELOCIDADE

            if tecla[pygame.K_s] and info.Y_PERSONAGEM < 630:
                info.Y += info.VELOCIDADE
                info.Y_PERSONAGEM += info.VELOCIDADE
                
                 
            if self.direcao == "direita" and info.X_PERSOINIMIGO < 1215:
                info.X_PERSOINIMIGO += info.VELOCIDADE
                  
            if self.direcao == "esquerda" and info.X_PERSOINIMIGO > 1000:
                info.X_PERSOINIMIGO -= info.VELOCIDADE  
                
            if self.direcao == "cima" and info.Y_PERSOINIMIGO > 20:
                info.Y_PERSOINIMIGO -= info.VELOCIDADE 
                
            if self.direcao == "baixo" and info.Y_PERSOINIMIGO < 650:
                info.Y_PERSOINIMIGO += info.VELOCIDADE

           
            #######################################     
            
            
            self.tiro.atualizar(info.VELOTIRO, True)
            self.tiroInimigo.atualizar(info.VELOTIRO, False)
            self.verificarTiros()
            
            
            if info.PONTOS < 0:
                self.controle = False
                jogando = False
                pygame.mixer.music.stop()


            ###############################
            self.detalhes.mostrarTexto(f"Pontos: {info.PONTOS}", 25,info.VERMELHO,50,0)
            
            ###################################
            
            #PASSAGEM DAS IMAGENS
            self.scrol += 5
            
            controleTempo = pygame.time.get_ticks()
            
            if controleTempo - self.intervalo >= 5000:
                self.num += 2
                self.intervalo = controleTempo
            ############################################
            
            pygame.display.update()

    #EFEITO PARALLAX CASO NECESSARIO
    def cenario(self):
        for x in range(self.num):
            for e in self.bg_imagens:
                self.tela.blit(e,((x * self.bg_width) - self.scrol,0)) 

            
    def verificarTiros(self):
        for tiro in self.tiro.tiros:
            tiro_surface = tiro["surface"]

            if self.mascara_persoInimigo and tiro_surface:
                mascara_tiro = pygame.mask.from_surface(tiro_surface)
                if mascara_tiro.overlap(self.mascara_persoInimigo,(info.X_PERSOINIMIGO - tiro["x"], info.Y_PERSOINIMIGO - tiro["y"])):
                    info.PONTOS += 5
                    self.tiro.tiros.remove(tiro)

        for tiro in self.tiroInimigo.tiros:
            tiro_surface = tiro["surface"]

            if self.mascara_personagem and tiro_surface:
                mascara_tiro = pygame.mask.from_surface(tiro_surface)
                if mascara_tiro.overlap(self.mascara_personagem, (info.X_PERSONAGEM - tiro["x"], info.Y_PERSONAGEM - tiro["y"])):
                    info.PONTOS -= 5
                    self.tiroInimigo.tiros.remove(tiro)


           
