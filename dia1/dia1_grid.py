import pygame

# Configurações do grid
LINHAS, COLUNAS = 10, 10
TAM_CELULA = 40
LARGURA, ALTURA = COLUNAS * TAM_CELULA, LINHAS * TAM_CELULA

class Agente:
    def __init__(self, linha=0, coluna=0):
        self.linha = linha
        self.coluna = coluna
        self.direcao = 1

    def mover(self):
        nova_coluna = self.coluna + self.direcao
        if 0 <= nova_coluna < COLUNAS:
            self.coluna = nova_coluna
        else:
            self.direcao *= -1
            self.linha = (self.linha + 1) % LINHAS



def desenhar_grid(tela):
    for l in range(LINHAS):
        for c in range(COLUNAS):
            rect = pygame.Rect(c*TAM_CELULA, l*TAM_CELULA, TAM_CELULA, TAM_CELULA)
            pygame.draw.rect(tela, (60, 60, 60), rect, 1)

def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Agente no Grid")
    relogio = pygame.time.Clock()
    
    # Cria o agente (objeto)
    agente = Agente()
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        
        agente.mover()

        tela.fill((20, 20, 20))
        desenhar_grid(tela)

        centro = (
            agente.coluna * TAM_CELULA + TAM_CELULA // 2,
            agente.linha * TAM_CELULA + TAM_CELULA // 2
        )
        pygame.draw.circle(tela, (0, 200, 255), centro, TAM_CELULA // 3)

        pygame.display.flip()
        relogio.tick(6)

    pygame.quit()

if __name__ == "__main__":
    main()