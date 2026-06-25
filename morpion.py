import pygame, sys, random

pygame.init()
W, H = 600, 600
ROWS, COLS = 3, 3
SZ = W // 3

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Tic Tac Toe')
screen.fill((28, 170, 156))

board = [[0]*3 for _ in range(3)]

# Images PNG
circle_img = pygame.transform.scale(pygame.image.load('circle_PNG49.png'), (SZ-40, SZ-40))
cross_img = pygame.transform.scale(pygame.image.load('10727988.png'), (SZ-40, SZ-40))

def draw_lines():
    for i in range(1, 3):
        pygame.draw.line(screen, (23,145,135), (0, i*SZ), (W, i*SZ), 15)
        pygame.draw.line(screen, (23,145,135), (i*SZ, 0), (i*SZ, H), 15)

def draw_board():
    for r in range(3):
        for c in range(3):
            x, y = c*SZ + 20, r*SZ + 20
            if board[r][c] == 1: screen.blit(circle_img, (x, y))
            elif board[r][c] == 2: screen.blit(cross_img, (x, y))

def check_win(p):
    for i in range(3):
        if all(board[i][j]==p for j in range(3)) or all(board[j][i]==p for j in range(3)): return True
    return all(board[i][i]==p for i in range(3)) or all(board[i][2-i]==p for i in range(3))

def full(): return all(board[r][c] != 0 for r in range(3) for c in range(3))

def random_move():
    moves = [(r,c) for r in range(3) for c in range(3) if board[r][c]==0]
    return random.choice(moves) if moves else None

def end(msg):
    s = pygame.Surface((W,H))
    s.set_alpha(180); s.fill((0,0,0))
    screen.blit(s, (0,0))
    txt = pygame.font.SysFont("comicsansms", 60, bold=True).render(msg, True, (255,255,255))
    screen.blit(txt, txt.get_rect(center=(W//2, H//2)))
    pygame.display.update()

    def minimax(board, depth, is_maximizing):
        if check_win(2): return 1
        if check_win(1): return -1
        if full(): return 0

        if is_maximizing:
            best_score = -float('inf')
            for r in range(3):
                for c in range(3):
                    if board[r][c] == 0:
                        board[r][c] = 2
                        score = minimax(board, depth + 1, False)
                        board[r][c] = 0
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for r in range(3):
                for c in range(3):
                    if board[r][c] == 0:
                        board[r][c] = 1
                        score = minimax(board, depth + 1, True)
                        board[r][c] = 0
                        best_score = min(score, best_score)
            return best_score

# Initialisation
draw_lines()
player = 1
game_over = False
ai_mode = "random"  # Options: "random" or "minimax"   
    
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_r:
            board = [[0]*3 for _ in range(3)]
            screen.fill((28,170,156))
            draw_lines()
            game_over = False
            player = 1

        if e.type == pygame.MOUSEBUTTONDOWN and not game_over and player == 1:
            r, c = e.pos[1]//SZ, e.pos[0]//SZ
            if 0 <= r < 3 and 0 <= c < 3 and board[r][c] == 0:
                board[r][c] = 1
                draw_board()

                if check_win(1): end("Joueur gagne !"); game_over = True
                elif full(): end("Match nul !"); game_over = True
                else: player = 2

    if player == 2 and not game_over:
        pygame.time.wait(300)
        move = random_move()
        if move:
            board[move[0]][move[1]] = 2
            draw_board()
            if check_win(2): end("IA gagne !"); game_over = True
            elif full(): end("Match nul !"); game_over = True
            else: player = 1

    pygame.display.update()