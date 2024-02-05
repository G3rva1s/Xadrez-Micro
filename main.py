import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações
largura, altura = 600, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tabuleiro de Xadrez")
clock = pygame.time.Clock()




#Imagens
BACTÉRIA = pygame.image.load('bac.jpg')
VIRUS = pygame.image.load('virus.jpg')
MACROFAGO = pygame.image.load('macrof.jpg')


tamanho_imgs = (60, 60)  # Novo tamanho desejado
BACTÉRIA = pygame.transform.scale(BACTÉRIA, tamanho_imgs)
VIRUS = pygame.transform.scale(VIRUS, tamanho_imgs)
MACROFAGO = pygame.transform.scale(MACROFAGO, tamanho_imgs)


# Cores
cor_branca = (255, 255, 255)
cor_preta = (0, 0, 0)
cor_cinza = (128, 128, 128)


# Contador de rodadas e timer
contador_rodadas = 0
tempo_restante = 5 * 60 * 1000  # 5 minutos em milissegundos
tempo_ultimo_frame = pygame.time.get_ticks()



contador_rodadas = 0
fonte = pygame.font.Font(None, 36)
p_fonte = pygame.font.Font(None, 21)

# Tamanho do tabuleiro e das casas
num_linhas, num_colunas = 10, 10
tamanho_casa = largura // num_colunas


# Contador de rodadas e timer
contador_rodadas = 0
tempo_restante = 5 * 60 * 1000  # 5 minutos em milissegundos
tempo_ultimo_frame = pygame.time.get_ticks()



#bordas cinzas


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


# Desenha o timer
def timer():
    minutos = tempo_restante // 60000
    segundos = (tempo_restante % 60000) // 1000
    texto_timer = fonte.render(f"Tempo", True, cor_preta)
    tela.blit(texto_timer, (8 * tamanho_casa + 5, 3 * tamanho_casa))
    
    texto_timer = fonte.render(f"Restante:", True, cor_preta)
    tela.blit(texto_timer, (8 * tamanho_casa + 5, 3 * tamanho_casa + 26))

    texto_minutos = fonte.render(f"{minutos:02d}:{segundos:02d}", True, cor_preta)
    tela.blit(texto_minutos, (8 * tamanho_casa + 15, 3 * tamanho_casa + 54))


   

    #tela.blit(texto_timer,(400, 200))

def desenhar_peças():
    tela.blit(BACTÉRIA, (0 * tamanho_casa, 0 * tamanho_casa))
    tela.blit(VIRUS, (3 * tamanho_casa, 0 * tamanho_casa))
    tela.blit(MACROFAGO,(3 *tamanho_casa, 9 * tamanho_casa))


# Função para desenhar o botão
def desenhar_botao():
    pygame.draw.rect(tela, cor_branca, botao)
    pygame.draw.rect(tela, cor_preta, botao, 2)  # Borda do botão
    texto_botao = p_fonte.render("Avançar Rodada", True, cor_preta)
    tela.blit(texto_botao, (botao.x + 10, botao.y + 10))

# Botão
botao = pygame.Rect(8 * tamanho_casa + 5, 1 * tamanho_casa, 110, 50)

#contador de rodadas
def rodadas():
    if botao.collidepoint(event.pos):
        contador_rodadas += 1


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
 
    timer()
    desenhar_botao()
    desenhar_peças()
    


    #contador de rodadas


    #energia cada jogador




    # Atualiza a tela
    pygame.display.flip()

    # Limita a taxa de atualização
    clock.tick(30)









#tabuleiro = [[(cor_branca if (i + j) % 2 == 0 else cor_preta)
               #for j in range(num_colunas)] for i in range(num_linhas)]

#desenhar bordas
#bordas =  #(cor_cinza if i == 0 or 9 else NONE)  