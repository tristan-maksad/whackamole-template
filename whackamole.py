import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        x_pos = 0
        y_pos = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if (event.type == pygame.MOUSEBUTTONDOWN) and (x_pos*640/20 <= event.pos[0] <= (x_pos + 1)*640/20) and (y_pos*512/16 <= event.pos[1] <= (y_pos + 1)*512/16):
                    x_pos = random.randrange(0,20)
                    y_pos = random.randrange(0,16)
            screen.fill("light green")

            for i in range(1,33):
                pygame.draw.line(screen, (0,0,0), (i*640/20, 0), (i*640/20, 512))
                pygame.draw.line(screen, (0, 0, 0), (0,i*512/16), (640,i*512/16))

            screen.blit(mole_image, mole_image.get_rect(topleft=(x_pos*640/20,y_pos*512/16)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()