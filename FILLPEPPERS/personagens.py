import pygame
import info
import os
import random

class Perso():

    def __init__(self, tela):
        self.tela = tela
        self.tiros = []

        self.larguraInimigo = None
        self.alturaInimigo = None
    

    ###CONFIGURAÇÕES DO TIRO
    def dispararTiro(self, xInfo, yInfo, veloTiro,verifica):
        if verifica:
            xTiro = xInfo + 70
            yTiro = yInfo 
        else:
            xTiro = xInfo - 40
            yTiro = yInfo + 10   
        tiroXpersonagem = xTiro
        tiroXinimigo = xTiro

        tiroVisivel = True

        if tiroVisivel:
            if verifica:
                tiroXpersonagem += veloTiro
                self.mostrarPersonagem(xTiro, yTiro)

                if tiroXpersonagem > 1300:
                    tiroVisivel = False

                if tiroXinimigo < -50:
                    tiroVisivel = False


                self.tiros.append({"x": tiroXpersonagem, "y": yTiro})
                self.tiros.append({"x": tiroXinimigo, "y": yTiro})
            else:
                tiroXinimigo -= veloTiro
                self.mostrarPersonagem(xTiro, yTiro)

                if tiroXpersonagem > 1300 or tiroXinimigo < -50:
                    tiroVisivel = False

                self.tiros.append({"x": tiroXpersonagem, "y": yTiro})
                self.tiros.append({"x": tiroXinimigo, "y": yTiro})

    def atualizar(self, veloTiro, verifica):
        for tiro in self.tiros:
            if verifica == True:
                tiro["x"] += veloTiro
                self.mostrarPersonagem(tiro["x"], tiro["y"])
            else:
                tiro["x"] -= veloTiro
                self.mostrarPersonagem(tiro["x"], tiro["y"])
    ##############      

    def mostrarPersonagem(self, x_personagem, y_personagem):
        self.tela.blit(self.personagens, (x_personagem,y_personagem))


    def criarPersonagem(self, direPerso):
        direImagem = os.path.join(os.getcwd(), "imagens")
        self.personagens = os.path.join(direImagem, direPerso)
        self.personagens = pygame.image.load(self.personagens).convert_alpha()  
        self.larguraInimigo, self.alturaInimigo = self.personagens.get_size()


    def bot(self, x,y,xPerso,yPerso,velo):
        direcao = random.choice(["cima", "baixo", "esquerda", "direita"])

        if direcao == "direita":
            x += velo
            xPerso += velo
        if direcao == "esquerda":
            x -= velo
            xPerso -= velo
        if direcao == "cima":
            y -= velo
            yPerso -= velo
        if direcao == "baixo":
            y += velo
            yPerso += velo    

        x = max(0,min(x,info.LARGURA - self.larguraInimigo))
        y = max(0, min(x, info.ALTURA - self.alturaInimigo))
        print(direcao)
