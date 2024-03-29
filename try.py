import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações
largura, altura = 600, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tabuleiro de Xadrez")
clock = pygame.time.Clock()

# Cores
cor_branca = (255, 255, 255)
cor_preta = (0, 0, 0)
cor_cinza = (128, 128, 128)

# Contador de rodadas e timer
contador_rodadas = 0
tempo_restante = 5 * 60 * 1000  # 5 minutos em milissegundos
tempo_ultimo_frame = pygame.time.get_ticks()

fonte = pygame.font.Font(None, 36)

# Tamanho do tabuleiro e das casas
num_linhas, num_colunas = 10, 10
tamanho_casa = largura // num_colunas

# Inicializa o tabuleiro
def init_tabuleiro():
    tabuleiro = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            if i in (0, 9) or j in (8, 9):
                linha.append(cor_cinza)
            elif i == 3 and j == 8:
                linha.append((255, 0, 0))  # Cor vermelha para o timer
            elif (i + j) % 2 == 0:
                linha.append(cor_branca)
            else:
                linha.append(cor_preta)
        tabuleiro.append(linha)
    return tabuleiro

# Desenha o timer
def timer():
    minutos = tempo_restante // 60000
    segundos = (tempo_restante % 60000) // 1000
    texto_timer = fonte.render(f"Tempo Restante:{minutos:02d}:{segundos:02d}", True, cor_preta)
    tela.blit(texto_timer, (8 * tamanho_casa, 3 * tamanho_casa))

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Obtém a posição do mouse
            pos_mouse = pygame.mouse.get_pos()
            coluna_selecionada = pos_mouse[0] // tamanho_casa
            linha_selecionada = pos_mouse[1] // tamanho_casa
            print(f"Casa selecionada: ({linha_selecionada}, {coluna_selecionada})")

    # Limpa a tela
    tela.fill(cor_branca)

    # Desenha o tabuleiro
    for i in range(num_linhas):
        for j in range(num_colunas):
            pygame.draw.rect(tela, init_tabuleiro()[i][j], (j * tamanho_casa, i * tamanho_casa, tamanho_casa, tamanho_casa))

    # Desenha o timer
    timer()

    # Atualiza a tela
    pygame.display.flip()

    # Limita a taxa de atualização
    clock.tick(30)
