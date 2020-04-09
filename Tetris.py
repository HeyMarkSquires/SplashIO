import pygame
import random
import serial
from time import sleep
import numpy as np
import pickle

filename = 'finalized_model.sav'
model = pickle.load(open(filename, 'rb'))
pygame.font.init()

#p=[[8.14,8.23,8.25,8.28,8.02,8.23,8.33,8.38,8.14,8.74,8.35,8.28,8.02,8.23,8.23,8.28,8.14,8.3,8.33,8.4,8.02,8.25,8.25,8.28,8.02,8.3,8.33,8.38,8.14,8.35,8.35,8.28,8.04,8.23,8.25,8.28,8.14,8.35,8.33,8.38,8.04,8.23,8.23,8.28,8.04,8.33,8.35,8.38,8.13,8.33,8.28,8.28,8.04,8.21,8.23,8.28,8.14,8.33,8.35,8.38,8.04,8.23,8.25,8.28,8.02,8.33,8.35,8.4,8.13,8.33,8.23,8.28,8.04,8.23,8.23,8.33,8.14,8.33,8.33,8.38]]
#r=np.array(p)
#print(model.predict(r))

s_width = 800
s_height = 700
play_width = 300  
play_height = 600  
block_size = 30
g_width=10
g_height=20

ser = serial.Serial('COM9', 9600)

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


#List of shapes
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapeList = [S, Z, I, O, J, L, T]
darkRed=(153, 0, 0)
moave=(204, 0, 153)
darkGreen=(0, 51, 0)
darkBlue=(102, 102, 153)
sandy=(255, 255, 204)
orange=(255, 153, 51)
greenBlue=(0, 204, 102)
shapeCols = [darkRed, moave, darkGreen, darkBlue, sandy, orange, greenBlue]

class Piece(object):  
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.colour = shapeCols[shapeList.index(shape)]
        self.angle = 0


def createGrid(locked_pos={}):
    grid = [[(0,0,0) for x in range(g_width)] for x in range(g_height)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j,i)]
                grid[i][j] = c
    return grid


def get_shape():
    global shapeList, shapeCols
    return Piece(5, 0, random.choice(shapeList))

def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.angle % len(shape.shape)]
 
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))
 
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
 
    return positions

def draw_text_middle(surface, text, size, colour):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, colour)
    
def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)
 
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
 
    return True

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

   
def draw_grid(surface, grid):
    # This function draws the grey grid lines that we see
    sx = top_left_x
    sy = top_left_y
    for i in range(len(grid)):
        pygame.draw.line(surface, (128,128,128), (sx, sy+ i*30), (sx + play_width, sy + i * 30))  # horizontal lines
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128,128,128), (sx + j * 30, sy), (sx + j * 30, sy + play_height))  # vertical lines

def clear_rows(grid, locked):
    inc = 0
    for i in range(len(grid)-1,-1,-1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            # add positions to remove from locked
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)

def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = shape.shape[shape.angle % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.colour, (sx + j*30, sy + i*30, 30, 30), 0)

    surface.blit(label, (sx + 10, sy- 30))

def draw_window(surface, grid, score=0, last_score = 0):
    surface.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont('papyrus', 60)
    label = font.render('Tetris', 1, (255, 255, 255))

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    sx = top_left_x - 200
    sy = top_left_y + 200

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)

    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)

    draw_grid(surface, grid)

def parser(data):
    sList=data.split()
    x=list(map(float, sList))
    result=np.array(x)
    return result

def main(win):
    global grid
    locked_positions = {}
    grid = createGrid(locked_positions)
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    count=0
    
    while run:
        state=[]
        prediction=5
        while count<20:
            val=ser.readline().decode("utf-8")
            x=parser(val)
            state[count]=x
            if count<19:
                count+=1
            else:
                g=state.flatten()
                v=[g]
                count=0
                print(g)
                print(v)
                prediction=model.predict(v)[0][0]
        fall_speed = 0.8
        grid = createGrid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()
        if fall_time/1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
            if event.type == pygame.KEYDOWN:

                #Moving the shape to the left
                if prediction == 3:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1

                #Moving the shape to the right
                elif prediction == 4:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1

                #Rotating shape
                elif prediction == 1:
                    current_piece.angle = current_piece.angle + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.angle - 1 % len(current_piece.shape)

                #Moving the shape down
                if prediction == 2:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                else:
                    
        shape_pos = convert_shape_format(current_piece)
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1: 
                grid[y][x] = current_piece.colour         
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.colour
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            clear_rows(grid, locked_positions)
    
        draw_window(win, grid)
        draw_next_shape(next_piece, win)
        pygame.display.update()
        
        if check_lost(locked_positions):
            draw_text_middle(win, "YOU LOST!", 80, (255,255,255))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False

def main_menu():
    run = True
    while run:
        val=ser.readline().decode("utf-8")
        state=np.zeros((20,4))
        win.fill((0,0,0))
        draw_text_middle(win, 'Press Any Key To Play', 60, (255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win)

    pygame.display.quit()

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Splash Tetris")
main_menu()
