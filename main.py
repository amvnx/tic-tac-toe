# pygame verstion of tic tac toe
import pygame as pg 
import sys 
import time 
from pygame.locals import *

# global variables used throughout game
game_board = [
  ['o', 'x', 'x'],
  ['o', 'o', 'o'], 
  ['x', 'o', 'x']
]
player_turn = 'x' 
winner = None
tie = None 

# hertz... 60hz 

O_COLOR = (0,0,0)
X_COLOR = (255,0,0)

# set game size
width = 400 
height = 400

# init pygame 
pg.init() 

CLOCK = pg.time.Clock()
fps = 30 

screen = pg.display.set_mode((width, height+100), 0, 32)

pg.display.set_caption("Tic Tac Toe") 

def game_init_window():
  pg.display.update() 
  time.sleep(1)
  screen.fill((0,255,255))
  # pg.draw.line(screen, line_color, )
  line_color = (0, 0, 255)
  pg.draw.line(screen, line_color, (width/3,0), (width/3,height), 5)
  pg.draw.line(screen, line_color, (width*2/3,0), (width*2/3,height), 5)
  pg.draw.line(screen, line_color, (0,height/3), (width, height/3), 5)
  pg.draw.line(screen, line_color, (0, height*2/3), (width,height*2/3), 5)

  line_color = (0,0,0)
  pg.draw.line(screen, line_color, (0, height), (width, height), 5)
  # clear out existing events
  pg.event.get()
''' 
  (0,0)       (width, 0)
    ----------
    |        |
    |        | height
    |        |
    |--------|
      width   (width,height)
(0,height)
'''

# game loop 
  # listen for events 
  # update state of game and objects
  # redraw all objects in game  


def check_win():
  global winner, tie 
  # loop rows
  for i in range(len(game_board)):
    if game_board[i][0] is not None and game_board[i][0] == game_board[i][1] and game_board[i][1] == game_board[i][2]:
      winner = game_board[i][0]
      return True

  # loop columns
  for i in range(len(game_board)):
      if game_board[0][i] is not None and game_board[0][i] == game_board[1][i] and game_board[1][i] == game_board[2][i]:
          winner = game_board[0][i]
          return True
  # check diagonals 
  if game_board[0][0] is not None and game_board[0][0] == game_board[1][1] and game_board[1][1] == game_board[2][2]:
      winner = game_board[0][0]
      return True
  if game_board[0][2] is not None and game_board[0][2] == game_board[1][1] and game_board[1][1] == game_board[2][0]:
      winner = game_board[0][2]
      return True
  tie = True 
  for i in range(len(game_board)):
    for j in range(len(game_board[i])):
      if game_board[i][j] is None:
        tie = False 
  if tie:
    return True 
  return False 

def reset_game():
  global game_board, player_turn, winner, tie
  game_board = [
    [None, None, None],
    [None, None, None], 
    [None, None, None]
  ]
  player_turn = 'x' 
  winner = None
  tie = None 
def drawXO(row, col):
  global player_turn 
  # draw an x or an o on the board 
  if player_turn =='x':
    drawX(row,col) 
  else:
    drawO(row,col)

def drawO(row,col):
  pg.draw.circle(screen, O_COLOR, (int(col*width/3+width/6), int(row*height/3+height/6)), 66,10)
def drawX(row,col):
  #draw our x 
  pg.draw.line(screen, X_COLOR, (col*width/3,row*height/3),(col*width/3+width/3, row*height/3+height/3),10)
  pg.draw.line(screen, X_COLOR, (col*width/3+width/3,row*height/3),(col*width/3, row*height/3+height/3),10)


def click():
  global game_board, player_turn
  x, y = pg.mouse.get_pos()
  print(x,y)
  row = 0
  col = 0 

  # figure out row 
  #   based on height and y 
  if y < height/3:
    row = 0
  elif y < 2*height/3:
    row = 1
  elif y < height:
    row = 2
  else:
    row = None

  # figure out col 
  #   based on width and x 
  if x < width/3:
    col = 0
  elif x < 2*width/3:
    col = 1
  elif x < width:
    col = 2
  else:
    col = None    

  if row is not None and col is not None:
    if game_board[row][col] is None:
      game_board[row][col] = player_turn 
      drawXO(row, col)
      # change player_turn to other player
      if player_turn == 'x':
        player_turn = 'o' 
      else: 
        player_turn = 'x'
      pg.display.update()

  print_game()

def print_game():
  s=""
  for i in range(len(game_board)):
      for j in range(len(game_board[i])):
        if game_board[i][j] == None:
          if i <2:
            s+="_"
          else:
            s+=" "
        else:
          s+=game_board[i][j]
        if j<2:
          s+="|"
      s+="\n"
  print(s)

def show_status(text):

  # fill status bar.
  screen.fill((0,0,0), (0, height,width,100))
  font = pg.font.Font(None, 30)
  text_obj = font.render(text, 1, (255,255,255))
  text_rect = text_obj.get_rect()
  text_rect.center =(width/2,height+50) 
  screen.blit(text_obj, text_rect)
  pg.display.update() 

reset_game()
game_init_window()

print
# game loop
while(True):
  # pg.event.get() 
  # write text status 
  show_status("Player " + player_turn+"'s turn")
  for event in pg.event.get():
    if event.type is MOUSEBUTTONDOWN:
      click() 
      if check_win():
        if tie:
          show_status("Draw")
        else:
          show_status(winner + " won.")
        time.sleep(3)
        show_status("New game is starting in 3..")
        time.sleep(1)
        show_status("New game is starting in 3..2..")
        time.sleep(1)
        show_status("New game is starting in 3..2..1..")
        reset_game()
        game_init_window()
      # write text status

  pg.display.update()
  CLOCK.tick(fps)
