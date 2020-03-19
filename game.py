import pygame, sys

ball_width = 100 
ball_height = 100 
player_width = 300
player_height = 25


class Ball(pygame.sprite.Sprite):

    ball_speed = 2 #??
    # position
    # direction

    def __init__(self):
        doge = pygame.image.load('images/doge.png')

        pygame.sprite.Sprite.__init__(self)
        self.width = ball_width
        self.height = ball_height
        self.image = doge
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        # Screen height/width and initial position of the ball
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.rect.x = int((self.screenwidth-self.width/2)/2)
        self.rect.y = int(self.screenheight-self.height-player_height)

    # bouncing function 
        # changes direction
        # bounces of and removes a block
        # bounces of walls
        # bounces of Player
        # sound

class Player(pygame.sprite.Sprite):
    # needs speed (possibly changing speed?)
    # position
    # direction - left and right

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([player_width, player_height])
        self.image.fill((117, 255, 7))
        self.rect = self.image.get_rect()

        self.rect.bottom = pygame.display.get_surface().get_height()
        self.rect.x = int(pygame.display.get_surface().get_height()/2)

class Block(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.width = int(pygame.display.get_surface().get_height()/5)
        self.height = 25

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

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

# Create sprite lists
blocks = pygame.sprite.Group()
balls = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

player = Player()
allsprites.add(player)

ball = Ball()
allsprites.add(ball)

# Block(self, x, y)
def row_of_blocks(block_row):
    # POsition to start rendering blocks
    block_column = 0 # 26, 52, 78 etc.
    for i in range(7):
            block = Block(block_column, block_row)
            blocks.add(block)
            allsprites.add(block)

            block_column = block_column + block.width + 2
            print(block_column)

    block_column = 0 # back to initial state
    # block_row += 30

block_row = 0 # block_height + 2
# create blocks
for row in range(8):
    row_of_blocks(block_row)
    block_row += 30

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
                exit_game = True
                print("closed with X")
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_game = True
                    print("closed with esc")
                    exit()

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

# if __name__ == '__main__': 
#     main()

# intro()
main_game()
