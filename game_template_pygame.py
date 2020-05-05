# packages needed
import pygame
import random

# creating colors(Red, Green, Blue)
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Cyan = (0, 255, 255)
Yellow = (255, 255, 0)
Purple = (255, 0, 255)

# forming the size of the window and frames per second
width = 1280
height = 720
FPS = 30

#  velocity of the object
vel = 10

# initiating the start/beginning/being of the game
pygame.init()
pygame.mixer.init()  # initiating sound
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tryna make it move")
clock = pygame.time.Clock()


# creating class that will have player's instance, named accordingly
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(Red)
        self.rect = self.image.get_rect()
        self.rect.center = (int(width / 2), int(height / 2))

    def update(self):
        if self.rect.top > height:  # if the side of the sprite is beyond the border,
            self.rect.bottom = 0  # it appears on the opposite side
        if self.rect.bottom > height:
            self.rect.top = 0
        if self.rect.left > width:
            self.rect.right = 0
        if self.rect.right > width:
            self.rect.left = 0


every_sprite = pygame.sprite.Group()  # group, bc why not))
player = Player()  # now, the player's instance is existing
every_sprite.add(player)  # player's instance is added to every_sprite group, bc that's more comfortable


# process of the game itself
running = True
while running:
    keys = pygame.key.get_pressed()
    clock.tick(FPS)  # making the game run at an acceptable speed
    for event in pygame.event.get():  # insertion of the events(literally making them exist)
        if event.type == pygame.QUIT:  # checking whether user clicked the X button
            running = False
    if keys[pygame.K_w] and player.rect.top > 0:
        player.rect.y -= vel
    if keys[pygame.K_s] and player.rect.bottom > 0:
        player.rect.y += vel
    if keys[pygame.K_a] and player.rect.left > 0:
        player.rect.x -= vel
    if keys[pygame.K_d] and player.rect.right > 0:
        player.rect.x += vel
    every_sprite.update()  # updating
    screen.fill(Black)  # rendering
    every_sprite.draw(screen)
    pygame.display.flip()  # flipping the display so the player would see everything

pygame.quit()
