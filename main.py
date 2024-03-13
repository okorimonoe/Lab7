import pygame

pygame.init()
screen_width, screen_height = 600, 300
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Pygame Game #1")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
screen.fill("White")
running = True

circle_x, circle_y = 50, 50
speed = 20

while running:
    screen.fill("White")

    pygame.draw.circle(screen, "Red", (circle_x, circle_y), 25)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                circle_y -= speed
            elif event.key == pygame.K_s:
                circle_y += speed
            elif event.key == pygame.K_a:
                circle_x -= speed
            elif event.key == pygame.K_d:
                circle_x += speed

    if circle_x < 25:
        circle_x = 25
    elif circle_x > screen_width - 25:
        circle_x = screen_width - 25
    if circle_y < 25:
        circle_y = 25
    elif circle_y > screen_height - 25:
        circle_y = screen_height - 25
