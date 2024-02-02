import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Move Sprite Example')

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define a custom sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, image_path, width, height):
        super().__init__()
        # Load the image from file
        original_image = pygame.image.load(image_path).convert_alpha()
        # Scale the image to the desired dimensions
        self.image = pygame.transform.scale(original_image, (width, height))
        # Get the rectangle that encloses the sprite image
        self.rect = self.image.get_rect()

# Create an instance of the custom sprite from a PNG file and resize it
my_sprite = MySprite('Images/player.png', 50, 50)  # Replace 'example_sprite.png' with your PNG file path, and set the desired width and height

# Set initial position of the sprite
my_sprite.rect.topleft = (screen_width // 2, screen_height // 2)

# Create a sprite group and add the sprite to it
sprite_group = pygame.sprite.Group()
sprite_group.add(my_sprite)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keyboard input for moving the sprite
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        my_sprite.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        my_sprite.rect.x += 5
    if keys[pygame.K_UP]:
        my_sprite.rect.y -= 5
    if keys[pygame.K_DOWN]:
        my_sprite.rect.y += 5

    # Clear the screen
    screen.fill(WHITE)

    # Draw the sprite
    sprite_group.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
