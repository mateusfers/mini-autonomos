import pygame
import random

LINHAS, COLUNAS = 10, 10
TAM_CELULA = 40

class Ambiente:
    def __init__(self):
        self.obstaculos = {
            (random.randint(0, LINHAS-1), random.randint(0, COLUNAS-1))
            for _ in range(8)
        }

    def percepcionar(self, linha, coluna):
        vizinhos = [
            (linha-1, coluna), (linha+1, coluna),
            (linha, coluna-1), (linha, coluna+1)
        ]
        return [v for v in vizinhos if v in self.obstaculos]

class AgenteAutonomo:
    def __init__(self, linha=0, coluna=0):
        self.linha = linha
        self.coluna = coluna

    def decidir(self, obstaculos_percebidos, destino):
        candidatos = [
            (self.linha+1, self.coluna), (self.linha-1, self.coluna),
            (self.linha, self.coluna+1), (self.linha, self.coluna-1)
        ]
        candidatos = [
            c for c in candidatos
            if c not in obstaculos_percebidos
            and 0 <= c[0] < LINHAS and 0 <= c[1] < COLUNAS
        ]
        if not candidatos:
            return self.linha, self.coluna
        candidatos.sort(key=lambda c: abs(c[0]-destino[0]) + abs(c[1]-destino[1]))
        return candidatos[0]

def main():
    pygame.init()
    tela = pygame.display.set_mode((COLUNAS*TAM_CELULA, LINHAS*TAM_CELULA))
    pygame.display.set_caption("Dia 4 - Do Grid a Decisao Autonoma")
    relogio = pygame.time.Clock()

    ambiente = Ambiente()
    agente = AgenteAutonomo()
    destino = (LINHAS-1, COLUNAS-1)
    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        percebidos = ambiente.percepcionar(agente.linha, agente.coluna)
        agente.linha, agente.coluna = agente.decidir(percebidos, destino)

        tela.fill((20, 20, 20))

        for (l, c) in ambiente.obstaculos:
            pygame.draw.rect(tela, (200, 50, 50), (c*TAM_CELULA, l*TAM_CELULA, TAM_CELULA, TAM_CELULA))

        pygame.draw.rect(tela, (50, 200, 100), (destino[1]*TAM_CELULA, destino[0]*TAM_CELULA, TAM_CELULA, TAM_CELULA))

        pygame.draw.circle(tela, (0, 200, 255), 
            (agente.coluna*TAM_CELULA+TAM_CELULA//2, agente.linha*TAM_CELULA+TAM_CELULA//2), 
            TAM_CELULA//3)

        pygame.display.flip()
        relogio.tick(3)

        if (agente.linha, agente.coluna) == destino:
            rodando = False

    pygame.quit()

if __name__ == "__main__":
    main()


