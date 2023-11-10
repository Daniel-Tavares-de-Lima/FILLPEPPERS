import pygame
import os 
import info


class GameOver:
    def __init__ (self,tela):
        self.tela = tela
        direImagens = os.path.join(os.getcwd(), "imagens")
        self.fonte = pygame.font.match_font(info.FONTE)
        self.arquivos()


    def arquivos(self):
        direImagens = os.path.join(os.getcwd(), "imagens")
        self.gameOverTela = os.path.join(direImagens, "galaxy.png")
        self.gameOverTela = pygame.image.load(self.gameOverTela).convert()


    def gameOver(self):
        gameOverBackground = self.gameOverTela.get_rect()
        self.tela.blit(self.gameOverTela, gameOverBackground)
        self.mostrarTexto("GAME OVER!", 32,info.VERMELHO,info.LARGURA//2, 320)
        self.mostrarTexto("Desenvolvido por Daniel Tavares",14, info.BRANCO,info.LARGURA//2,640)
        pygame.display.flip()
        


    def mostrarTexto(self, texto, tamanho, cor,x,y):
        #Exiber texto
        fonte = pygame.font.Font(self.fonte, tamanho)
        texto = fonte.render(texto, False, cor)
        textoRect = texto.get_rect()
        textoRect.midtop = (x,y)
        self.tela.blit(texto, textoRect)            
    