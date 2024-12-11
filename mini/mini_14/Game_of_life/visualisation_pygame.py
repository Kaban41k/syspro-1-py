import pygame
import generator_np as gen
import sys

sys.setrecursionlimit(10**9)

WIDTH, HEIGHT = 800, 800

CELL_SIZE = 4

DELAY = 10

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

f = gen.Field(WIDTH//CELL_SIZE, HEIGHT//CELL_SIZE)
f.generate_field()


def draw_field(screen):
    for y in range(f.height):
        for x in range(f.width):
            if f.field[y][x]:
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game of life")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_field(screen)
        pygame.display.flip()
        pygame.time.delay(DELAY)
        f.next_iteration()

    pygame.quit()


if __name__ == "__main__":
    main()
