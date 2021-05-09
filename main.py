import pygame
import gameClass
import os

game = gameClass.Window()
colors = gameClass.Colors()

def render():
    game.WIN.fill(colors.MINT)
    game.draw_sprite("p1")
    pygame.display.update()

def main():
    running = True
    clock = pygame.time.Clock()
    game.new_sprite("p1", (10, 10), (116, 137), "./Player.png")

    while running:
        clock.tick(game.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        render()
    pygame.quit()

if __name__ == "__main__":
    main()