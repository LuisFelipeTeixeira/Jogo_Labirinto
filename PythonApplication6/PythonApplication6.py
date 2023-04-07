import pygame
import time
import sys

# Constantes
WIDTH = 600
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

def draw_maze(screen, maze):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                rect = pygame.Rect(col*WIDTH//len(maze[row]), row*HEIGHT//len(maze), WIDTH//len(maze[row]), HEIGHT//len(maze))
                pygame.draw.rect(screen, BLACK, rect)

def move_player(maze, player_row, player_col, exit_row, exit_col):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_col > 0 and maze[player_row][player_col-1] != 1:
        player_col -= 1
    elif keys[pygame.K_RIGHT] and player_col < len(maze[0])-1 and maze[player_row][player_col+1] != 1:
        player_col += 1
    elif keys[pygame.K_UP] and player_row > 0 and maze[player_row-1][player_col] != 1:
        player_row -= 1
    elif keys[pygame.K_DOWN] and player_row < len(maze)-1 and maze[player_row+1][player_col] != 1:
        player_row += 1

        
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Labirinto')

    # Verificando se o jogador chegou à saída
    if player_row == exit_row and player_col == exit_col:
        font = pygame.font.Font(None, 72)
        win_text = font.render('Voce Venceu!', True, GREEN)
        screen.blit(win_text, [WIDTH//2 - win_text.get_width()//2, HEIGHT//2 - win_text.get_height()//2])
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    return player_row, player_col

def main():
    # Inicializando o Pygame
    pygame.init()

    # Criando a janela
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Labirinto')

    # Definindo o labirinto
    maze = [
        [0, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0],
    ]

    # Definindo a posição inicial do jogador e a posição da saída
    player_row, player_col = 0, 0
    exit_row, exit_col = len(maze)-1, len(maze[0])-1
   # Loop principal do jogo
    while True:
        # Tratando eventos da janela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movendo o jogador
        player_row, player_col = move_player(maze, player_row, player_col, exit_row, exit_col)

        # Desenhando o labirinto e o jogador na tela
        screen.fill(WHITE)
        draw_maze(screen, maze)
        player_rect = pygame.Rect(player_col*WIDTH//len(maze[0]), player_row*HEIGHT//len(maze), WIDTH//len(maze[0]), HEIGHT//len(maze))
        pygame.draw.rect(screen, GREEN, player_rect)

        # Atualizando a tela
        pygame.display.update()

        # Verificando se o jogo deve ser encerrado
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    main()

