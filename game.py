import pygame, sys

class Ball(pygame.sprite.Sprite):
    # needs speed
    # position
    # direction

    # background
    # shape / size

    # bouncing function 
        # changes direction
        # bounces of and removes a block
        # bounces of walls
        # bounces of Player
        # sound
    pass

class Player(pygame.sprite.Sprite):
    # needs speed (possibly changing speed?)
    # position
    # direction - left and right managed below

    # width / height 
    # background
    pass

class Block(pygame.sprite.Sprite):
    # needs width / height 
    # colour
    # position
    pass
# how many blocks?

# Initialize pygame
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

game_over = False
game_won = False
exit_game = False
intro = True 


def main_game():
# Main loop 
    while 1:
        if game_over:
            print("Game over!")
            print("Play again?")

        if game_won:
            print("Game won!")
            print("Play again?")

        # Quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_program = True
                print("closed with X")
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_program = True
                    print("closed with esc")
                    exit()

        screen.blit(background, (0, 0))
        pygame.display.flip()

# if __name__ == '__main__': 
#     main()

# intro()
main_game()
