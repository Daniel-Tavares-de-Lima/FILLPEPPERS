import pygame
import info
import os
import random
import neat

class Perso():

    def __init__(self, tela):
        self.tela = tela
        self.tiros = []

        self.larguraInimigo = None
        self.alturaInimigo = None
        self.personagens = None
        self.geracao = 0
        self.tiroXpersonagem = 0
        self.tiroXinimigo = 0
        self.xTiro = 0
        self.yTiro = 0
        
    

    ###CONFIGURAÇÕES DO TIRO
    def dispararTiro(self, xInfo, yInfo, veloTiro,verifica):
        if verifica:
            self.xTiro = xInfo + 70
            self.yTiro = yInfo 
        else:
            self.xTiro = xInfo - 40
            self.yTiro = yInfo + 10   
        self.tiroXpersonagem = self.xTiro
        self.tiroXinimigo = self.xTiro

        self.mascaraTiroPersonagem = pygame.mask.from_surface(self.personagens)

        tiroVisivel = True

        if tiroVisivel:
            if verifica:
                self.tiroXpersonagem += veloTiro
                self.mostrarPersonagem(self.xTiro, self.yTiro)

                if self.tiroXpersonagem > 1300:
                    tiroVisivel = False

                self.tiros.append({"x": self.tiroXpersonagem, "y": self.yTiro, "surface": self.personagens})
                self.tiros.append({"x": self.tiroXinimigo, "y": self.yTiro, "surface": self.personagens})

                for tiro in self.tiros:
                    tiro["mascara"] = pygame.mask.from_surface(self.personagens)
            else:
                self.tiroXinimigo -= veloTiro
                self.mostrarPersonagem(self.xTiro, self.yTiro)

                if self.tiroXinimigo < -50:
                    tiroVisivel = False

                self.tiros.append({"x": self.tiroXpersonagem, "y": self.yTiro, "surface": self.personagens})
                self.tiros.append({"x": self.tiroXinimigo, "y": self.yTiro, "surface": self.personagens})

                for tiro in self.tiros:
                    tiro["mascara"] = pygame.mask.from_surface(self.personagens)

    def atualizar(self, veloTiro, verifica):
        for tiro in self.tiros:
            if verifica == True:
                tiro["x"] += veloTiro
                self.mostrarPersonagem(tiro["x"], tiro["y"])
            else:
                tiro["x"] -= veloTiro
                self.mostrarPersonagem(tiro["x"], tiro["y"])

        



    def mostrarPersonagem(self, x_personagem, y_personagem):
        self.tela.blit(self.personagens, (x_personagem,y_personagem))


    def criarPersonagem(self, direPerso):
        direImagem = os.path.join(os.getcwd(), "imagens")
        self.personagens = os.path.join(direImagem, direPerso)
        self.personagens = pygame.image.load(self.personagens).convert_alpha()  
        self.larguraInimigo, self.alturaInimigo = self.personagens.get_size()
        self.geracao += 1
        self.mascaraPersonagem = pygame.mask.from_surface(self.personagens)

    def mostrarTexto(self, texto, tamanho, cor,x,y):
        #Exiber texto
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, False, cor)
        textoRect = texto.get_rect()
        textoRect.midtop = (x,y)
        self.tela.blit(texto, textoRect) 


    

        
