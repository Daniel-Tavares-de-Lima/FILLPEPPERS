import pygame
import os 
import info
from detalhes import Details

class GameOver:
    def __init__ (self,tela):
        self.tela = tela
        direImagens = os.path.join(os.getcwd(), "imagens")
        self.fonte = pygame.font.match_font(info.FONTE)
        self.arquivos()
        self.detalhes = Details(tela)


    def arquivos(self):
        direImagens = os.path.join(os.getcwd(), "imagens")
        self.gameOverTela = os.path.join(direImagens, "galaxy.png")
        self.gameOverTela = pygame.image.load(self.gameOverTela).convert()


    def gameOver(self):
        gameOverBackground = self.gameOverTela.get_rect()
        self.tela.blit(self.gameOverTela, gameOverBackground)
        self.detalhes.mostrarTexto("GAME OVER!", 32,info.VERMELHO,info.LARGURA//2, 320)
        self.detalhes.mostrarTexto("Desenvolvido por Daniel Tavares",14, info.BRANCO,info.LARGURA//2,640)
        pygame.display.flip()
        

   
    