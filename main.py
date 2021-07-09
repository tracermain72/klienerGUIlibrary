import sys

from KlienerGuiLibrary import *

pygame.init()

FPS = 60
SIZE = WIDTH, HEIGHT = (200, 200)
BGCOLOR = (20,20,20)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

#Creates a text and text_rect that is centered.
# text, text_rect = returnKlienerTextCentered("timesnewroman", 30, "brr", (255,255,255), (WIDTH/2, HEIGHT/2), True)

#Creates a text and text_rect that is -not- centered.
# text, text_rect = returnKlienerText("timesnewroman", 30, "brr", (255,255,255), (WIDTH/2, HEIGHT/2), True)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  screen.fill(BGCOLOR)

  #Blits the word brr onto the screen and is centered.
  #drawKlienerTextCentered("timesnewroman", 30, "brr", (255,255,255), (WIDTH/2, HEIGHT/2), True, screen)
  
  #Blits the word brr onto the screen.
  #drawKlienerText("timesnewroman", 30, "brr", (255,255,255), (WIDTH/2, HEIGHT/2), True, screen)

  pygame.display.update()
  clock.tick(FPS)