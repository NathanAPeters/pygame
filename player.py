import pygame

# Constants for player
PLAYER_SPEED = 1500
WALL_JUMP_STRENGTH = (10, 15)
WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)  # Starting position
        self.velocity = pygame.math.Vector2(0, 0)
        self.direction_facing = pygame.math.Vector2(1, 0)
        self.on_wall_status = "inAir"
        self.is_dashing = False
    
    def update(self):
        keys = pygame.key.get_pressed()
        
        if not self.is_dashing:
            direction = 0
            if keys[pygame.K_LEFT]:
                direction = -1
                if self.on_wall_status != "rightWall":
                    self.velocity.x = PLAYER_SPEED * direction * 0.016
                    self.direction_facing = pygame.math.Vector2(-1, 0)
            elif keys[pygame.K_RIGHT]:
                direction = 1
                if self.on_wall_status != "leftWall":
                    self.velocity.x = PLAYER_SPEED * direction * 0.016
                    self.direction_facing = pygame.math.Vector2(1, 0)
            else:
                self.velocity.x = 0

        self.rect.x += self.velocity.x
    
    def handle_collision(self, other):
        if other.tag == "Wall":
            if other.rect.x > self.rect.x:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    self.velocity = pygame.math.Vector2(WALL_JUMP_STRENGTH[0], -WALL_JUMP_STRENGTH[1])
                    self.on_wall_status = "leftWall"
                else:
                    self.on_wall_status = "OnWall"
            elif other.rect.x < self.rect.x:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    self.velocity = pygame.math.Vector2(-WALL_JUMP_STRENGTH[0], -WALL_JUMP_STRENGTH[1])
                    self.on_wall_status = "rightWall"
                else:
                    self.on_wall_status = "OnWall"
            else:
                self.on_wall_status = "inAir"

    def on_collision_exit(self, other):
        if other.tag == "Wall":
            self.on_wall_status = "inAir"