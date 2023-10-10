import pygame
import info
import os




class Game():
    
    
    def __init__(self, tela):
        
        self.tela = tela
        self.personagens = None
        self.relogio = pygame.time.Clock()
        
        
        
        
        
        
    def telaJogo(self):

        direImagens = os.path.join(os.getcwd(), "Imagens")
        self.personagens = os.path.join(direImagens, info.PERSONAGEM)
        self.personagens = pygame.image.load(self.personagens).convert_alpha()
        
        jogando = True
        
        
        controleDeTeclas = set()

        while jogando:
            self.relogio.tick(4)
            self.tela.fill(info.PRETO)
            self.movimentarPersonagem()
            pygame.display.flip()
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    jogando = False
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    controleDeTeclas.add(evento.key)

                elif evento.type == pygame.KEYUP:
                    controleDeTeclas.discard(evento.key)

            if len(controleDeTeclas) == 1:
                tecla = pygame.key.get_pressed()

                if tecla[pygame.K_w]:
                    info.Y_SOLDADO -=15
                    info.Y_PERSONAGEM = 3
                    info.X_PERSONAGEM += 1

                if tecla[pygame.K_a]:
                    info.X_SOLDADO -= 15
                    info.Y_PERSONAGEM = 1
                    info.X_PERSONAGEM += 1

                if tecla[pygame.K_d]:
                    info.X_SOLDADO += 15
                    info.Y_PERSONAGEM = 2
                    info.X_PERSONAGEM += 1

                if tecla[pygame.K_s]:
                    info.Y_SOLDADO += 15
                    info.Y_PERSONAGEM = 0
                    info.X_PERSONAGEM += 1

            if info.X_PERSONAGEM > 3:
                info.X_PERSONAGEM = 0

           
    
    def movimentarPersonagem(self):
        
        # startPersonagem = self.personagens.get_rect()
        # startPersonagem.midtop = (x,y)  
        self.tela.blit(self.personagens, (info.X_SOLDADO, info.Y_SOLDADO), (info.X_PERSONAGEM * 65, info.Y_PERSONAGEM * 95,60,90)) 