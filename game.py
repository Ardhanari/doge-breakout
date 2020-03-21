import pygame, sys
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 
BALL_WIDTH = 100 
BALL_HEIGHT = 100 
PLAYER_WIDTH = 300
PLAYER_HEIGHT = 25


class Ball(pygame.sprite.Sprite):

    speed = 3 #??
    # position
    dir = 300 # degrees 

    # x = int((SCREEN_WIDTH-BALL_WIDTH/2)/2)
    # y = int(SCREEN_HEIGHT-BALL_HEIGHT-PLAYER_HEIGHT)
    x = 200
    y = 600 - BALL_HEIGHT

    def __init__(self):
        doge = pygame.image.load('images/doge.png')

        pygame.sprite.Sprite.__init__(self)
        self.width = BALL_WIDTH
        self.height = BALL_HEIGHT
        self.image = doge
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        # Screen height/width and initial position of the ball
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.rect.x = int((self.screenwidth-self.width/2)/2)
        self.rect.y = int(self.screenheight-self.height-PLAYER_HEIGHT)
        

    def horizontal_bounce(self, diff):
        self.dir = (180 - self.dir) % 360
        self.dir -= diff
    
    def move(self):
        print(self.rect.x)
        dir_radians = math.radians(self.dir)

        self.rect.x += self.speed * math.sin(dir_radians)
        self.rect.y -= self.speed * math.cos(dir_radians)

        # Bouncing off the top wall
        if self.rect.y <= 0:
            pygame.mixer.music.play()
            self.horizontal_bounce(0)
            print("bounced off top)")
            self.rect.y = 1
        # Boucing off the left wall
        if self.rect.x <= 0:
            pygame.mixer.music.play()
            print("bounced off left")
            self.dir = (360 - self.dir) % 360
            self.rect.x = 1
        # Boucing off the right wall
        if self.rect.x >= self.screenwidth - BALL_WIDTH:
            pygame.mixer.music.play()
            self.dir = (360 - self.dir) % 360
            self.rect.x = self.screenwidth - BALL_WIDTH - 1
        # Bounce off player
        # if pygame.sprite.spritecollide(ball, player, False):
        #     pygame.mixer.music.play()
            # do what now? 
        # Ball touches bottom wall
        if self.rect.y > SCREEN_HEIGHT:
            # pygame.mixer.music.play() play another sound?
            return True # will return true to game_over variable

class Player(pygame.sprite.Sprite):
    
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill((117, 255, 7))
        self.rect = self.image.get_rect()

        self.rect.bottom = pygame.display.get_surface().get_height()
        self.rect.x = int(pygame.display.get_surface().get_height()/2)

    # def move(self):
    #     # position = self.rect.x
    #     # print(self.rect.x)
    #     pass

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
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set background color
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((245, 216, 148))

# Set the title
pygame.display.set_caption('Doge breakout (wow)')

# Define font
font = pygame.font.Font(pygame.font.match_font('comicsansms'), 55) # I am SO sorry

clock = pygame.time.Clock()

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
    for i in range(10):
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

        if intro: 
        #     text = font.render("Much game, wow", 1, (10, 10, 10))
        #     textpos = text.get_rect()
        #     textpos.centerx = background.get_rect().centerx
        #     background.blit(text, textpos)
        #     # text = font.render("You win!", True, BLACK)
        #     # text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        #     # screen.blit(text, text_rect)

        #     screen.blit(background, (0, 0))
        #     pygame.display.flip()
        #     pygame.mixer.music.load('sounds/intro.mp3')
        #     pygame.mixer.music.play()
        #     pygame.mixer.music.fadeout(6000)
            pygame.mixer.music.load('sounds/pop.mp3')
        #     # to be moved to bounce function
        #     # pygame.mixer.music.play()
            
            
            intro = False
        # screen.fill((0,0,0))

        if not game_over or not game_won: 

            # player.move()
            ball.move()     

            # check for ball colliding with walls 
            # if pygame.sprite.collide_rect(ball, blocks):
            bounced_blocks = pygame.sprite.spritecollide(ball, blocks, True)
            if len(bounced_blocks) > 0: 
                pygame.mixer.music.play()
            print(bounced_blocks)
            print(len(blocks))

            if len(blocks) == 0:
                game_won = True
                print("Game won!")
                print("Play again?")


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.rect.x -= 20
                        # player.move()
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

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        clock.tick(30)
        pygame.display.flip()


# if __name__ == '__main__': 
#     main()

# intro()
main_game()
