# https://github.com/EgorLz/PyGame.git
import pygame

def draw(screen):
    screen.fill('yellow')
    font = pygame.font.Font(None, 200)
    text = font.render('NAVI', True, 'black')
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    draw(screen)

    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()
