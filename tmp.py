from tkinter import Y


x=10*5
y=9*10
z=x*y 
print(x)
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
running = True

x = 47
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill((255, 255, 255)) # apaga o quadro atual

  # Lógica de jogo e renderização do novo quadro
  figura = pygame.Surface([30, 30]) # cria uma superfície quadrada com 30 pixels de lado
  figura.fill((0, 0, 0)) # preenche a superfície com cor preta
  screen.blit(figura, (x, 200)) # desenha figura sobre o quadro atual nas coordenadas indicadas
  x = x + 3 # avança 3 pixels a cada quadro

  pygame.display.flip() # Desenha o quadro atual na tela
  clock.tick(60)

pygame.quit()
