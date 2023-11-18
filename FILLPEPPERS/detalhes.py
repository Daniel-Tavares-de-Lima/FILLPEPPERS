import pygame
import info
import os


class Details:
    def __init__ (self,tela):
        self.tela = tela
        self.fonte = pygame.font.match_font(info.FONTE)
        self.carregarArquivos()
        self.background = None
        self.gameOverTela = None
        self.direSom = None
        
    def mostrarTexto(self, texto, tamanho, cor,x,y):
        #Exiber texto
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, False, cor)
        textoRect = texto.get_rect()
        textoRect.midtop = (x,y)
        self.tela.blit(texto, textoRect)       


    def carregarArquivos(self):
        direImagens = os.path.join(os.getcwd(), "imagens")
        self.background = os.path.join(direImagens, "TelaStart.png")
        self.background = pygame.image.load(self.background).convert()
        self.direSom = os.path.join(os.getcwd(), "sons")