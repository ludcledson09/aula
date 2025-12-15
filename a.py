import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill((255, 255, 255)) # apaga o quadro atual

  # Lógica de jogo e renderização do novo quadro
  figura = pygame.Surface([30, 30]) # cria uma superfície quadrada com 30 pixels de lado
  figura.fill((0, 0, 0)) # preenche a superfície com cor preta
  screen.blit(figura, (50, 200)) # desenha figura sobre o quadro atual nas coordenadas indicadas

  pygame.display.flip() # Desenha o quadro atual na tela
  clock.tick(60)

pygame.quit()
