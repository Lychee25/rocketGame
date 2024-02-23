import pygame
from pygame.locals import*
import time
pygame.init()

keys = [False, False, False, False] #0 - up key, 1- left, 2 - down, 3 - right
speed = 70

screen = pygame.display.set_mode((500, 500))

img = pygame.image.load("space.jpg")
space = pygame.transform.scale(img, (500, 500))
img2 = pygame.image.load("rocket.png")
rocket = pygame.transform.scale(img2, (90, 70))
rocketX = 200
rocketY = 80

while rocketY <= 500:
  screen.blit(space, (0,0))
  screen.blit(rocket, (rocketX, rocketY))
  pygame.display.update()

  for events in pygame.event.get():
    if events.type == pygame.QUIT:
      pygame.quit()
      exit(0)
    if events.type == pygame.KEYDOWN:
      if events.key == K_UP:
        keys[0] = True
      if events.key == K_DOWN:
        keys[2] = True
      if events.key == K_LEFT:
        keys[1] = True
      if events.key == K_RIGHT:
        keys[3] = True
    if events.type == pygame.KEYUP:
      if events.key == K_UP:
        keys[0] = False
      if events.key == K_DOWN:
        keys[2] = False
      if events.key == K_LEFT:
        keys[1] = False
      if events.key == K_RIGHT:
        keys[3] = False

  if keys[0] == True:
    rocketY = rocketY - speed
    if rocketY < 15:
      rocketY = rocketY + speed
  elif keys[2] == True:
    rocketY = rocketY + speed
  elif keys[1] == True:
    rocketX = rocketX - speed
    if rocketX < 15:
      rocketX = rocketX + speed
  elif keys[3] == True:
    rocketX = rocketX + speed
    if rocketX > 450:
      rocketX = rocketX - speed
  rocketY = rocketY + 20
  time.sleep(0.25)