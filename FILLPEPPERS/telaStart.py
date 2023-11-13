import pygame
from pygame.locals import *
from sys import exit
import info 
from fases import Fases
import os
from gameOver import GameOver
from detalhes import Details


class Start:
    #Construtor
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((info.LARGURA, info.ALTURA))
        pygame.display.set_caption(info.TITULO_JOGO)
        self.executando = True
        self.relogio = pygame.time.Clock()
        self.fonte = pygame.font.match_font(info.FONTE)
        # self.carregarArquivos()
        self.fases = Fases(self.tela)
        self.detalhes = Details(self.tela)
        self.detalhes.carregarArquivos()

    def rodar(self):
        
        self.jogando = True
        
        while self.jogando:
            
            if self.fases.controle:
                self.controleTela("start")
            else:
                self.controleTela("gameOver") 

            self.relogio.tick(info.FPS)
            self.eventos()
            
        

    def controleTela(self, telaDestino):
        if telaDestino == "start":
            self.fases = Fases(self.tela)
            self.fases.fase1()
        elif telaDestino == "gameOver":
            self.gameOver = GameOver(self.tela)
            self.gameOver.gameOver()
        
    def eventos(self):
        for evento in pygame.event.get():
            if evento.type == QUIT:

                if self.jogando:
                    self.jogando = False
                    pygame.quit()
                    exit()


    def telaStart(self):
        startBackground = self.detalhes.background.get_rect()
        self.tela.blit(self.detalhes.background, startBackground)
        self.detalhes.mostrarTexto("Pressione qualquer tecla para jogar", 32,info.VERMELHO,info.LARGURA//2, 320)
        self.detalhes.mostrarTexto("Desenvolvido por Daniel Tavares",14, info.BRANCO,info.LARGURA//2,690)
        # pygame.mixer.music.load(os.path.join(self.detalhes.direSom, "musicaDeFundo.mp3"))
        # pygame.mixer.music.play()
        pygame.display.flip()
        self.esperarPorJogador()


    def esperarPorJogador(self):
        rodando = True
        while rodando:
            self.relogio.tick(info.FPS)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.executando = False   
                if evento.type == pygame.KEYUP:
                    rodando = False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(os.path.join(self.detalhes.direSom, "Token.wav")).play()
                    


g = Start()
g.telaStart()
while g.executando:
    g.rodar()
    