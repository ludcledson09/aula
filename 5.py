import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 24)
mouse_x, mouse_y = 0, 0
texto_1, texto_2 = None, "Sem clique"
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    elif event.type == pygame.MOUSEMOTION:
      mouse_x = event.pos[0]
      mouse_y = event.pos[1]
    elif event.type == pygame.MOUSEBUTTONDOWN:
      texto_2 = f"Último clique: botão {event.button} em ({event.pos[0]}, {event.pos[1]}) "
  screen.fill((255, 255, 255))
  surface_texto_1 = font.render(f"Posição: {mouse_x}, {mouse_y}", True, 'black')
  screen.blit(surface_texto_1, (15, 15))
  surface_texto_2 = font.render(texto_2, True, 'black')
  screen.blit(surface_texto_2, (15, 40))
  pygame.display.flip()
  clock.tick(60)
