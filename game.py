import pygame

def main():
    pygame.init()

    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])

    # Set background color
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((245, 216, 148))
    
    # Set the title
    pygame.display.set_caption('Doge breakout (wow)')

    # Define font
    font = pygame.font.Font(pygame.font.match_font('comicsansms'), 55) # I am SO sorry
    text = font.render("Much game, wow", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Manage keyboard 
    while 1:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
        	            return
                    if event.key == pygame.K_LEFT:                        
                        # move player left
                        pass
                    if event.key == pygame.K_RIGHT:                    
                        #move player right
                        pass

        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': 
    main()