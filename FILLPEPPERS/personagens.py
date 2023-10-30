import pygame
import info
import os

class Perso():

    def __init__(self, tela):
        self.tela = tela
        
        


    def mostrarPersonagem(self, x_personagem, y_personagem):
        self.tela.blit(self.personagens, (x_personagem,y_personagem))


    def criarPersonagem(self, direPerso):
        direImagem = os.path.join(os.getcwd(), "imagens")
        self.personagens = os.path.join(direImagem, direPerso)
        self.personagens = pygame.image.load(self.personagens).convert_alpha()  

