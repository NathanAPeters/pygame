import pygame
from pygame.locals import *
from player import Player

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.tag = "Wall"

# Setup the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('2D Game')

# Create game objects
player = Player()
walls = pygame.sprite.Group()
walls.add(Wall(300, 400, 100, 50), Wall(500, 300, 100, 50))

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(walls)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    all_sprites.update()
    
    # Check for collisions
    for wall in walls:
        if pygame.sprite.collide_rect(player, wall):
            player.handle_collision(wall)
        else:
            player.on_collision_exit(wall)
    
    # Draw everything
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    
    clock.tick(FPS)

pygame.quit()