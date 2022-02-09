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


class Display:
    def __init__(self, caption='Tic-Tac-Toe', width=WIDTH, height=HEIGHT, font='Comic Sans MS', fontsize=30, bg_color=WHITE):
        self.caption = caption
        self.width = width
        self.height = height
        self.font = font
        self.fontsize = fontsize
        self.bg_color = bg_color
        self.screen = None
        self.box_size = None
        self.board = np.zeros((ROWS, COLUMNS))
        self.CIRCLE = pygame.image.load('circle.png')
        self.CROSS = pygame.image.load('cross.png')

    def draw_lines(self):

        self.box_size = math.sqrt((self.height*self.width)/9)
        self.box_size = self.box_size/(self.width/self.height)
        pygame.draw.line(self.screen, BLACK, (self.box_size, 0), (self.box_size, self.box_size*3), 10)
        pygame.draw.line(self.screen, BLACK, (self.box_size*2, 0), (self.box_size*2, self.box_size*3), 10)
        pygame.draw.line(self.screen, BLACK, (0, self.box_size), (self.box_size*3, self.box_size), 10)
        pygame.draw.line(self.screen, BLACK, (0, self.box_size*2), (self.box_size*3, self.box_size*2), 10)

    def is_winning_move(self, player):

        winning_colour = player.colour
        print(self.board)
        for sing_row in range(ROWS):
            if self.board[sing_row][0] == player.id and self.board[sing_row][1] == player.id and self.board[sing_row][2] == player.id:
                pygame.draw.line(self.screen, winning_colour, (10, (sing_row*self.box_size) + math.floor(self.box_size/2)), ((self.box_size*3)-10, (sing_row*self.box_size) + math.floor(self.box_size/2)), 10)
                return True

        for sing_col in range(COLUMNS):
            if self.board[0][sing_col] == player.id and self.board[1][sing_col] == player.id and self.board[2][sing_col] == player.id:
                pygame.draw.line(self.screen, winning_colour, ((sing_col*self.box_size) + math.floor(self.box_size/2), 10), ((sing_col*self.box_size) + math.floor(self.box_size/2), (self.box_size*3)-10), 10)
                return True

        if self.board[0][0] == player.id and self.board[1][1] == player.id and self.board[2][2] == player.id:
            pygame.draw.line(self.screen, winning_colour, (10, 10), (math.floor(self.box_size*3)-10, math.floor(self.box_size*3)-10), 10)
            return True

        elif self.board[0][2] == player.id and self.board[1][1] == player.id and self.board[2][0] == player.id:
            pygame.draw.line(self.screen, winning_colour, (math.floor(self.box_size*3)-10, 10), (10, math.floor(self.box_size*3)-10), 10)
            return True
        else:
            return False

    def initialize_screen(self):

        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.bg_color)
        pygame.display.set_caption(self.caption)
        self.draw_lines()
        pygame.display.update()

    def draw_board(self, player):
        self.CIRCLE = pygame.transform.scale(self.CIRCLE, (self.box_size-math.floor(self.box_size*0.25), self.box_size-math.floor(self.box_size*0.25)))
        self.CROSS = pygame.transform.scale(self.CROSS, (self.box_size-math.floor(self.box_size*0.25), self.box_size-math.floor(self.box_size*0.25)))

        if player.choice == 'X':
            choice = self.CROSS
        else:
            choice = self.CIRCLE

        for col in range(COLUMNS):
            for row in range(ROWS):
                if self.board[row][col] == player.id:
                    self.screen.blit(choice, ((col*self.box_size)+math.floor(self.box_size*(0.25/2)), (row*self.box_size)+math.floor(self.box_size*(0.25/2))))
        pygame.display.update()

    def mark(self, row, col, player):
        self.board[row][col] = player.id

    def is_valid_mark(self, row, col):
        return self.board[row][col] == 0

    def check_draw(self):
        return False if 0 in self.board else True

    def restart_game(self):
        print("Game Over!")
        pygame.time.delay(2000)
        self.board.fill(0)
        self.screen.fill(WHITE)
        self.draw_lines()
        pygame.display.update()


class Player:
    def __init__(self, player_id, player_colour, sign_choice, player_name=None):
        self.id = player_id
        self.player_name = player_name
        self.colour = player_colour
        self.choice = sign_choice


if __name__ == '__main__':
    window = Display()
    window.initialize_screen()

    player1 = Player(3, RED, 'X')
    player2 = Player(4, BLUE, 'O')

    game_over = False

    player_turn = 0

    running = True
    while not game_over:
        for event in pygame.event.get():
            print(f"{event=}")
            if event.type == pygame.QUIT:
                game_over = True
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                if player_turn % 2 == 0:
                    #  player 1
                    now_player = player1
                    if event.pos[1] <= window.box_size*3 and event.pos[0] <= window.box_size*3:
                        row = math.floor(event.pos[1]/window.box_size)
                        col = math.floor(event.pos[0]/window.box_size)
                        if window.is_valid_mark(row, col):
                            window.mark(row, col, player1)
                            if window.is_winning_move(player1):
                                print("WINNING MOVE!?")
                                game_over = True
                            if window.check_draw():
                                game_over = True
                        else:
                            player_turn -= 1
                    else:
                        player_turn -= 1
                    print("Player 1")
                else:
                    #  player 2
                    now_player = player2
                    if event.pos[1] <= window.box_size*3 and event.pos[0] <= window.box_size*3:
                        row = math.floor(event.pos[1]/window.box_size)
                        col = math.floor(event.pos[0]/window.box_size)
                        if window.is_valid_mark(row, col):
                            window.mark(row, col, player2)
                            if window.is_winning_move(player2):
                                print("WINNING MOVE 2!?")
                                game_over = True
                            if window.check_draw():
                                game_over = True
                        else:
                            player_turn -= 1
                    else:
                        player_turn -= 1
                    print("Player 2")

                player_turn += 1
                window.draw_board(now_player)

        if game_over and running:
            window.restart_game()
            game_over = False
