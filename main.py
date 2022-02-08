import numpy as np
import pygame
import math

ROWS = 3
COLUMNS = 3

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WIDTH = 1280
HEIGHT = 720
WINDOW = (WIDTH, HEIGHT)

CIRCLE = pygame.image.load('circle.png')
CROSS = pygame.image.load('cross.png')

box_size = 0

def mark(row, col, player):
    board[row][col] = player


def is_valid_mark(row, col):
    return board[row][col] == 0


def is_board_full():
    for col in range(COLUMNS):
        for row in range(ROWS):
            if board[row][col] == 0:
                return False
    return True


def check_draw():
    return False if 0 in board else True


def draw_board():
    global CIRCLE
    global CROSS
    global box_size

    CIRCLE = pygame.transform.scale(CIRCLE, (box_size-math.floor(box_size*0.25), box_size-math.floor(box_size*0.25)))
    CROSS = pygame.transform.scale(CROSS, (box_size-math.floor(box_size*0.25), box_size-math.floor(box_size*0.25)))


    for col in range(COLUMNS):
        for row in range(ROWS):
            if board[row][col] == 1:
                screen.blit(CROSS, ((col*box_size)+math.floor(box_size*(0.25/2)), (row*box_size)+math.floor(box_size*(0.25/2))))
            if board[row][col] == 2:
                screen.blit(CIRCLE, ((col*box_size)+math.floor(box_size*(0.25/2)), (row*box_size)+math.floor(box_size*(0.25/2))))
    pygame.display.update()

def draw_lines():

    global box_size
    box_size = math.sqrt((HEIGHT*WIDTH)/9)
    box_size = box_size/(WIDTH/HEIGHT)
    pygame.draw.line(screen, BLACK, (box_size, 0), (box_size, box_size*3), 10)
    pygame.draw.line(screen, BLACK, (box_size*2, 0), (box_size*2, box_size*3), 10)
    pygame.draw.line(screen, BLACK, (0, box_size), (box_size*3, box_size), 10)
    pygame.draw.line(screen, BLACK, (0, box_size*2), (box_size*3, box_size*2), 10)


def is_winning_move(player):
    if player == 1:
        winning_colour = RED
    else:
        winning_colour = BLUE
    for sing_row in range(ROWS):
        if board[sing_row][0] == player and board[sing_row][1] == player and board[sing_row][2] == player:
            print("FIRST IF")
            pygame.draw.line(screen, winning_colour, (10, (sing_row*box_size) + math.floor(box_size/2)), ((box_size*3)-10, (sing_row*box_size) + math.floor(box_size/2)), 10)
            return True
    for sing_col in range(COLUMNS):
        if board[0][sing_col] == player and board[1][sing_col] == player and board[2][sing_col] == player:
            print("SECOND IF")
            pygame.draw.line(screen, winning_colour, ((sing_col*box_size) + math.floor(box_size/2), 10), ((sing_col*box_size) + math.floor(box_size/2), (box_size*3)-10), 10)
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print("THIRD IF")
        pygame.draw.line(screen, winning_colour, (10, 10), (math.floor(box_size*3)-10, math.floor(box_size*3)-10), 10)
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print("FOURTH IF")
        pygame.draw.line(screen, winning_colour, (math.floor(box_size*3)-10, 10), (10, math.floor(box_size*3)-10), 10)
        return True
    else:
        print("FIFTH IF")
        return False

if __name__ == '__main__':

    game_over = False
    board = np.zeros((ROWS, COLUMNS))

    player_turn = 0

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(WINDOW)
    pygame.display.set_caption("Tic-Tac-Toe")
    screen.fill(WHITE)
    draw_lines()
    pygame.display.update()
    pygame.time.wait(2000)
    game_font = pygame.font.SysFont('Comic Sans MS', 30)

    running = True
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                print(box_size)
                if player_turn % 2 == 0:
                    #  player 1
                    if event.pos[1] <= box_size*3 and event.pos[0] <= box_size*3:
                        row = math.floor(event.pos[1]/box_size)
                        col = math.floor(event.pos[0]/box_size)
                        if is_valid_mark(row, col):
                            mark(row, col, 1)
                            if is_winning_move(1):
                                win_text = game_font.render('Player 1 won the game!', True, (255, 0, 0))
                                win_text_rect = win_text.get_rect(center=(math.floor(box_size*1.5), math.floor(box_size*1.5)))
                                screen.blit(win_text, win_text_rect)
                                pygame.display.update()
                                game_over = True
                            if check_draw():
                                win_text = game_font.render('Draw!', True, (255, 0, 0))
                                win_text_rect = win_text.get_rect(center=(math.floor(box_size*1.5), math.floor(box_size*1.5)))
                                screen.blit(win_text, win_text_rect)
                                pygame.display.update()
                                game_over = True
                        else:
                            player_turn -= 1
                    else:
                        player_turn -= 1
                    print("Player 1")
                else:
                    #  player 2
                    if event.pos[1] <= box_size*3 and event.pos[0] <= box_size*3:
                        row = math.floor(event.pos[1]/box_size)
                        col = math.floor(event.pos[0]/box_size)
                        if is_valid_mark(row, col):
                            mark(row, col, 2)
                            if is_winning_move(2):

                                win_text = game_font.render('Player 2 won the game!', False, (255, 0, 0))
                                win_text_rect = win_text.get_rect(center=(math.floor(box_size*1.5), math.floor(box_size*1.5)))
                                screen.blit(win_text, win_text_rect)
                                pygame.display.update()
                                game_over = True
                            if check_draw():

                                win_text = game_font.render('Draw!', False, (255, 0, 0))
                                win_text_rect = win_text.get_rect(center=(math.floor(box_size*1.5), math.floor(box_size*1.5)))
                                screen.blit(win_text, win_text_rect)
                                pygame.display.update()
                                game_over = True
                        else:
                            player_turn -= 1
                    else:
                        player_turn -= 1
                    print("Player 2")

                player_turn += 1
                print(board)
                draw_board()

        if game_over and running:
            print("Game Over!")
            pygame.time.wait(2000)
            board.fill(0)
            screen.fill(WHITE)
            draw_lines()
            draw_board()
            game_over = False
            pygame.display.update()