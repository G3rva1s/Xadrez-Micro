import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações
largura, altura = 800, 600
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

# Fonte
fonte = pygame.font.Font(None, 36)

# Tamanho do tabuleiro e das casas
num_linhas, num_colunas = 10, 10
tamanho_casa = largura // num_colunas

# Posições
area_cinza_x = largura - 200
area_cinza_largura = 200

# Inicializa o tabuleiro
def init_tabuleiro():
    tabuleiro = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            if i in (0, 9) or j in (8, 9):
                linha.append(cor_cinza)
            elif (i + j) % 2 == 0:
                linha.append(cor_branca)
            else:
                linha.append(cor_preta)
        tabuleiro.append(linha)
    return tabuleiro

# Função para desenhar o botão
def desenhar_botao():
    pygame.draw.rect(tela, cor_branca, botao)
    pygame.draw.rect(tela, cor_preta, botao, 2)  # Borda do botão
    texto_botao = fonte.render("Avançar Rodada", True, cor_preta)
    tela.blit(texto_botao, (botao.x + 10, botao.y + 10))

# Botão
botao = pygame.Rect(area_cinza_x + 10, 10, 180, 50)

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if botao.collidepoint(event.pos):
                contador_rodadas += 1

    # Atualiza o timer
    tempo_atual = pygame.time.get_ticks()
    tempo_passado = tempo_atual - tempo_ultimo_frame
    tempo_ultimo_frame = tempo_atual
    tempo_restante -= tempo_passado

    # Limpa a tela
    tela.fill(cor_branca)

    # Desenha o tabuleiro
    for i in range(num_linhas):
        for j in range(num_colunas):
            pygame.draw.rect(tela, init_tabuleiro()[i][j], (j * tamanho_casa, i * tamanho_casa, tamanho_casa, tamanho_casa))

    # Desenha a área cinza
    pygame.draw.rect(tela, cor_cinza, (area_cinza_x, 0, area_cinza_largura, altura))

    # Desenha o botão
    desenhar_botao()

    # Desenha o contador de rodadas
    texto_contador = fonte.render(f"Rodadas: {contador_rodadas}", True, cor_preta)
    tela.blit(texto_contador, (area_cinza_x + 10, 70))

    # Desenha o timer
    minutos = tempo_restante // 60000
    segundos = (tempo_restante % 60000) // 1000
    texto_timer = fonte.render(f"Tempo Restante: {minutos:02d}:{segundos:02d}", True, cor_preta)
    tela.blit(texto_timer, (area_cinza_x + 10, 120))

    # Atualiza a tela
    pygame.display.flip()

    # Limita a taxa de atualização
    clock.tick(30)
