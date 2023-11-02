import pygame
from pygame.locals import *
from sys import exit
import info 
from fases import Fases
import os



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
        self.carregarArquivos()


    def rodar(self):
        
        self.jogando = True
        while self.jogando:
            self.controleTela("start")
            self.relogio.tick(info.FPS)
            self.eventos()
            
        

    def controleTela(self, telaDestino):
        if telaDestino == "start":
            self.fases = Fases(self.tela)
            self.fases.fase1()
        elif telaDestino == "d":
            pass
        
    def eventos(self):
        for evento in pygame.event.get():
            if evento.type == QUIT:

                if self.jogando:
                    self.jogando = False
                    pygame.quit()
                    exit()

    def carregarArquivos(self):
        direImagens = os.path.join(os.getcwd(), "imagens")
        self.background = os.path.join(direImagens, "TelaStart.png")
        self.background = pygame.image.load(self.background).convert()
        

    def mostrarTexto(self, texto, tamanho, cor,x,y):
        #Exiber texto
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, False, cor)
        textoRect = texto.get_rect()
        textoRect.midtop = (x,y)
        self.tela.blit(texto, textoRect)           

    
        
    def telaStart(self):
        startBackground = self.background.get_rect()
        self.tela.blit(self.background, startBackground)

        self.mostrarTexto("Pressione qualquer tecla para jogar", 32,info.VERMELHO,info.LARGURA//2, 320)
        self.mostrarTexto("Desenvolvido por Daniel Tavares",14, info.BRANCO,info.LARGURA//2,690)
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
                    print(rodando)


g = Start()
g.telaStart()
while g.executando:
    g.rodar()
    