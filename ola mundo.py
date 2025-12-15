import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 480)) # configura janela do jogo
clock = pygame.time.Clock()
running = True

while running:
  # Processamento de eventos (entradas de teclado e mouse)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Apaga o quadro atual preenchendo a tela com a cor preta
  screen.fill((255, 255, 255))

  # Lógica de jogo e renderização do novo quadro

  # Desenha o quadro atual na tela
  pygame.display.flip()

  clock.tick(60)  # Pausa e indica a taxa de quadros por segundo (FPS)

pygame.quit()
