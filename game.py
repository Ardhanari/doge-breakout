import pygame, sys
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 
BALL_WIDTH = 75
BALL_HEIGHT = 75
PLAYER_WIDTH = 300
PLAYER_HEIGHT = 25


class Ball(pygame.sprite.Sprite):

    speed = 7
    dir = 300 # degrees 
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
        # Ball touches bottom wall
        if self.rect.y >= SCREEN_HEIGHT-BALL_HEIGHT:
            return True
        else:
            return False


class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill((117, 255, 7))
        self.rect = self.image.get_rect()

        self.rect.bottom = pygame.display.get_surface().get_height()
        self.rect.x = int(pygame.display.get_surface().get_height()/2)
        # player can't move out of the screen
        # if self.rect.x <= 0:
        #     self.rect.x = 1
        # if self.rect.x >= SCREEN_WIDTH - PLAYER_WIDTH:
        #     self.rect.x = SCREEN_WIDTH - PLAYER_WIDTH - 1


class Block(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.width = 77.8
        self.height = 25

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

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
balls.add(ball)
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

    block_column = 0 # back to initial state

block_row = 0 # block_height + 2
# create blocks
for row in range(3):
    row_of_blocks(block_row)
    block_row += 30

def main_game():
    
    game_over = False
    game_won = False
    intro = True 
    sound = True
    
    # Main loop 
    while not game_won:

        if intro: 
            text = font.render("Much game, wow", 1, (10, 10, 10))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            info = pygame.image.load('images/info.png')
            infopos = info.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            background.blit(text, textpos)
            background.blit(info, infopos)
            screen.blit(background, (0, 0))
            pygame.display.flip()
            pygame.mixer.music.load('sounds/intro.mp3')
            pygame.mixer.music.play()
            pygame.mixer.music.fadeout(6000)
            pygame.mixer.music.load('sounds/pop.mp3')
            hide_title = pygame.Surface(screen.get_size())
            hide_title = background.convert()
            hide_title.fill((245, 216, 148))
            background.blit(hide_title, (0, 0))
            intro = False

        if not game_won: 

            game_over = ball.move()

            # Bounce off player
            # if pygame.sprite.spritecollide(player, balls, False):
            if pygame.sprite.collide_rect(player, ball):
                pygame.mixer.music.play()
                diff = (player.rect.x + PLAYER_WIDTH/2) - (ball.rect.x + BALL_WIDTH/2) # glitches, check math
                
                # ball.horizontal_bounce(diff)
                ball.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT - BALL_HEIGHT - 1
                print(ball.rect.y)
                print(diff)
                ball.horizontal_bounce(diff)

            # check for ball colliding with walls 
            bounced_blocks = pygame.sprite.spritecollide(ball, blocks, True)
            if len(bounced_blocks) > 0: 
                pygame.mixer.music.play()
                ball.horizontal_bounce(0)

            # check if player touches the wall
            if player.rect.x <= 0:
                player.rect.x = 0
            if player.rect.x >= SCREEN_WIDTH - PLAYER_WIDTH:
                player.rect.x = SCREEN_WIDTH - PLAYER_WIDTH

            if len(blocks) == 0:
                game_won = True
            #     background = pygame.Surface(screen.get_size())
            #     background = background.convert()
            #     background.fill((55, 55, 148))
            #     screen.blit(background, (0, 0))
            #     pygame.mixer.music.load('sounds/game_won.wav') # needs to play ONCE
            #     pygame.mixer.music.play()
            #     pygame.mixer.music.stop()
            #     text = font.render("You won, wow", 1, (10, 10, 10))
            #     text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            #     screen.blit(text, text_rect)
            #     pygame.display.flip()
            #     print("Game won!")
            #     print("Play again?")

            if game_over:
                if sound: 
                    pygame.mixer.music.load('sounds/game_over.wav')
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play()
                    sound = False
                ball.speed = 0
                text = font.render("Gaem over", 1, (10, 10, 10))
                text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
                screen.blit(text, text_rect)
                pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.rect.x -= 20
                        print("left")
                    if event.key == pygame.K_RIGHT:
                        player.rect.x += 20
                        print("right")
                    # Quit game (Escape)
                    if event.key == pygame.K_ESCAPE:
                            print("closed with esc")
                            exit()    
                # Quit game (x)
                if event.type == pygame.QUIT:
                    print("closed with X")
                    exit()

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        clock.tick(30) # 30 fps
        pygame.display.flip()

    while game_won:

        if sound:
            pygame.mixer.music.load('sounds/intro.mp3') # needs to play ONCE
            pygame.mixer.music.play(-1) # actually, let's make it a loop 
            sound = False
        
        background_won = pygame.Surface(screen.get_size())
        background_won = background_won.convert()
        background_won.fill((55, 55, 148))
        
        text = font.render("You won, wow", 1, (10, 10, 10))
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        
        screen.blit(background_won, (0, 0))
        screen.blit(text, text_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            # Quit game (Escape)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        print("closed with esc")
                        exit()    
            # Quit game (x)
            if event.type == pygame.QUIT:
                print("closed with X")
                exit()

main_game()
