import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (300,50)
import pygame
import pgzrun
import random
import time

    
TITLE = 'Apple Shot'
WIDTH = 800
HEIGHT = 600

#AppleActor
appleSprite = Actor('apple1')
appleSprite.pos = (0, random.randint(0, 590))
appleSprite.vy = 1
appleSpeed =5
#BombActor
bombSprite = Actor('bomb1')
bombSprite.pos = (0, random.randint(0, 590))
bombSprite.vy = 1
bombSpeed =5
#CrosshairActor
crosshairSprite = Actor('crosshair')
apple_shot = False
bomb_shot = False
#defuat game_state set
game_state = ''
score = 0

#apple movement
def appleMove():
      appleSprite.y = appleSprite.y + appleSprite.vy
      appleSprite.x = appleSprite.x + appleSpeed
      if (appleSprite.left > WIDTH or appleSprite.right < 0) :
          resetApple()

#bomb movement          
def bombMove():
      bombSprite.y = bombSprite.y + bombSprite.vy
      bombSprite.x = bombSprite.x + bombSpeed
      if (bombSprite.left > WIDTH or bombSprite.right < 0) :
            resetBomb()

            
#apple reset
def resetApple():
      global apple_speed
      appleSprite.vy = random.randint(-1, 1)
      appleSprite.pos = (random.randint(0,1)*800, random.randint(50, 400))
      #check the position that the sprite re-spawn
      if (appleSprite.x <= 0) : #left
          appleSpeed = random.randint (5, 10)
      else : #right
          appleSpeed = random.randint(-10, -5)

#bomb reset
def resetBomb():
      global bombSpeed
      bombSprite.vy = random.randint(-1, 1)
      bombSprite.pos = (random.randint(0,1)*800, random.randint(50, 400))
      if (bombSprite.x <= 0) :
          bombSpeed = random.randint (3, 8)
      else :
          bombSpeed = random.randint(-8, -3)

def on_mouse_move(pos, rel, buttons):
      crosshairSprite.x = pos[0]
      crosshairSprite.y = pos[1]

def on_mouse_down(pos, button):
      global apple_shot
      global bomb_shot
      global score
      global game_state
      if button == mouse.LEFT and (apple_shot == False and bomb_shot == False) :
          if appleSprite.collidepoint(pos):
              apple_shot == True
              score = score+1
              print('score =',score)
              resetApple()
              if score >= 5:
                  game_state = 'win'
          else :
              apple_shot == False
              
          if bombSprite.collidepoint(pos):
              bomb_shot == True
              game_state = 'gameover'
              print ('Game Over')
              resetBomb()
          else :
              bomb_shot == False

def update():
    global game_state
    appleMove()
    if apple_shot == True:
        appleSprite.image = 'apple2'
        appleSprite.y = applesprite.y + 12
        if appleSprite.y > HEIGHT:
            resetApple()
        if score >= 5:
            game_state = 'win'

    bombMove()
    if bomb_shot == True :
        bombSprite.image = 'bomb2'
        bombSprite.y = appleSprite.y + 12
        if appleSprite.y  > HEIGHT :
            reset_bomb()

def draw():
    global game_state
    screen.blit('background',(0,0))
    def restart():
        global game_state
        global score
        screen.draw.text('Press Spacebar to Play', center = (400,300), color = 'black', fontsize = 65)
        if keyboard.space == True :
            game_state = 'play'
            score = 0

    if game_state == '' :
        screen.draw.text('Apple Shot', center = (400,150), color = 'red', fontsize = 120)
        restart()
    elif game_state == 'win':
        screen.draw.text('Victory!', center = (400,150), color = 'red', fontsize = 120)
        restart()
    elif game_state == 'gameover':
        screen.draw.text('Game Over!', center = (400,150), color = 'red', fontsize = 120)
        restart()
    elif game_state == 'play':
        appleSprite.draw()
        bombSprite.draw()
        crosshairSprite.draw()
        screen.draw.text('score :' + str(score),(15,10), color = 'white', fontsize = 40)

pgzrun.go()
            











