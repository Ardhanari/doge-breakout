import pygame, sys

screen_width = 800
screen_height = 600 
ball_width = 100 
ball_height = 100 
player_width = 300
player_height = 25


class Ball(pygame.sprite.Sprite):

    speed = 1 #??
    # position
    direction = 300 # degrees 

    # x = int((screen_width-ball_width/2)/2)
    # y = int(screen_height-ball_height-player_height)
    x = 200
    y = 0 

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
        # bounces of Player
        # sound
    def move(self):
        # to figure out how angles work 
        self.x += self.speed * self.direction
        self.y += self.speed #+= what?

        self.rect.x = self.x
        self.rect.y = self.y

        # Bouncing off the top wall
        if self.rect.y <= 0:
            self.rect.y = 1
        # Boucing off the right wall
        if self.rect.x <= 0:
            self.rect.x = 1
        # Boucing off the left wall
        if self.rect.x >= self.screenwidth:
            self.rect.x = self.screenwidth - 1
        if self.rect.y > screen_height:
            # game over 
            pass

class Player(pygame.sprite.Sprite):
    
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([player_width, player_height])
        self.image.fill((117, 255, 7))
        self.rect = self.image.get_rect()

        self.rect.bottom = pygame.display.get_surface().get_height()
        self.rect.x = int(pygame.display.get_surface().get_height()/2)

    def move(self):
        # position = self.rect.x
        print(self.rect.x)

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
screen = pygame.display.set_mode([screen_width, screen_height])

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
            # print(block_column) # debug

    block_column = 0 # back to initial state
    # block_row += 30

block_row = 0 # block_height + 2
# create blocks
for row in range(8):
    row_of_blocks(block_row)
    block_row += 30

def main_game():
    
    game_over = False
    game_won = False
    exit_game = False
    intro = True 
    
    # Main loop 
    while not exit_game:

        # screen.fill((0,0,0))

        if not game_over or not game_won: 

            player.move()
            ball.move()        
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.rect.x -= 20
                        player.move()
                        print("left")
                    if event.key == pygame.K_RIGHT:
                        player.rect.x += 20
                        print("right")
                    # Quit game (Escape)
                    if event.key == pygame.K_ESCAPE:
                            exit_game = True
                            print("closed with esc")
                            exit()    
                # Quit game (x)
                if event.type == pygame.QUIT:
                    exit_game = True
                    print("closed with X")
                    exit()

        # Game finished (over, won or quit)
        if game_over:
            print("Game over!")
            print("Play again?")

        if game_won:
            print("Game won!")
            print("Play again?")

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

# if __name__ == '__main__': 
#     main()

# intro()
main_game()
