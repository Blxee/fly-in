import pygame
import sys

# 1. Initialize
pygame.init()

# 2. Create window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame")

# 3. Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close button
            running = False

    # Fill screen with color (R, G, B)
    screen.fill((30, 30, 30))

    # Draw a rectangle (x, y, width, height)
    pygame.draw.rect(screen, (255, 0, 0), (100, 100, 50, 50))
    pygame.draw.circle(screen, (0, 255, 0), (200, 100), 50)

    # Update the display
    pygame.display.flip()

# 4. Quit
pygame.quit()
sys.exit()
