import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
figura = pygame.Surface([30, 30])
figura.fill((0, 0, 0))
x = 50
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
     	  running = False
      elif event.key == pygame.K_RIGHT:
     	  x = x + 10
 	 
  screen.fill((255, 255, 255))
  screen.blit(figura, (x, 200))
  pygame.display.flip()
  clock.tick(60)
pygame.quit()
