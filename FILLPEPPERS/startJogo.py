import pygame
from pygame.locals import *
from sys import exit
from random import randint
from game import Game
import os

import info



class Start:

    #Isso é um construtor
    def __init__(self):
        #Criando a janela
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((info.LARGURA, info.ALTURA))
        pygame.display.set_caption(info.TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.rodando = True
        self.fonte = pygame.font.match_font(info.FONTE)
        self.carregarArquivos()

        # self.game = Game(self)
        self.game = None
        
    ##
    def comecar(self, telaDestino):
        if telaDestino == "jogo":
            self.game = Game(self.tela)
            self.game.telaJogo()
        elif telaDestino == "gameOver":
            self.gameOver()
        elif telaDestino == "outraTela":
            pass        
            
        

    def novoJogo(self):
        #instancia as classes das sprites do jogp
        self.todasSprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        #looping do jogo
        self.telaStart()
        self.jogando = True
        while self.jogando:
            self.comecar("jogo")##

            self.relogio.tick(info.FPS)
            #EVENTOS PARA TECLADO, MOUSE
            self.eventos()
            
            #COLISAO//ATUALIZAO
            self.atualizarSprites()
            self.desenharSprites()

    def eventos(self):
        #define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.rodando = False    

    def atualizarSprites(self):
        #atualiza os sprites
        self.todasSprites.update()

    def desenharSprites(self):
        self.tela.fill(info.PRETO) ##limpando a tela
        self.todasSprites.draw(self.tela) #desenhando as sprites
        pygame.display.flip()

    #CARREGAR OS ARQUIVOS
    def carregarArquivos(self):
        #Carregar os arquivos de audio e imagens
        direImagens = os.path.join(os.getcwd(), "Imagens")
        self.direAudios = os.path.join(os.getcwd(), "sounds")
        self.logoSprites = os.path.join(direImagens, info.LOGO)
        self.logoSprites = pygame.image.load(self.logoSprites).convert()

        self.personagemS = os.path.join(direImagens, info.PERSONAGEM)
        self.personagemS = pygame.image.load(self.personagemS).convert()

    def mostrarTexto(self, texto, tamanho, cor, x, y):
        #EXIBE TEXTO
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, False, cor)
        textoRect = texto.get_rect()
        textoRect.midtop = (x,y)
        self.tela.blit(texto, textoRect)

    def mostrarStartLogo(self, x,y):
        startLogoRect = self.logoSprites.get_rect()
        startLogoRect.midtop = (x,y)
        self.tela.blit(self.logoSprites, startLogoRect)


    def telaStart(self):
        self.mostrarStartLogo(info.LARGURA/ 2, 20)

        pygame.mixer.music.load(os.path.join(self.direAudios, info.AUDIO))
        pygame.mixer.music.play()

        self.mostrarTexto("Pressione qualquer tecla para jogar", 32, info.VERMELHO, info.LARGURA//2, 320)
        self.mostrarTexto("Desenvolvido por Daniel Tavares", 14, info.BRANCO, info.LARGURA//2, 550)
        pygame.display.flip()
        self.esperarPorJogador()

    def esperarPorJogador(self):
        esperando = True
        
        while esperando:
            self.relogio.tick(info.FPS)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    
                    self.rodando = False

                    if(self.rodando == False):
                        esperando = False

                if evento.type == pygame.KEYUP:
                    esperando = False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(os.path.join(self.direAudios, "Token.wav")).play()
                    
                    
                    
                    

                
    def gameOver(self):
        pass    




g = Start()
# startGame = Game(g)

g.telaStart()
while g.rodando:
    g.novoJogo()
    g.gameOver()







