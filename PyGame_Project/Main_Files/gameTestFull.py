import pygame
import sys
import os

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sample Screen")

# Load an image
image = pygame.image.load('Lvl1_1.png')


# Load a sound
pygame.mixer.init()
sound = pygame.mixer.Sound('TestAudio.mp3')

# Define button attributes
button_width, button_height = 200, 50
button_color = (0, 128, 255)
button_text_color = (255, 255, 255)

# Create two buttons
button1 = pygame.Rect(300, 450, button_width, button_height)
button2 = pygame.Rect(500, 450, button_width, button_height)

# Initialize font
font = pygame.font.Font(None, 36)

# Text for buttons
button_text1 = font.render("Button 1", True, button_text_color)
button_text2 = font.render("Button 2", True, button_text_color)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                # Button 1 action
                sound.play()
            elif button2.collidepoint(event.pos):
                # Button 2 action
                sound.play()

    # Display the image
    screen.blit(image, (0, 0))

    # Draw buttons
    pygame.draw.rect(screen, button_color, button1)
    pygame.draw.rect(screen, button_color, button2)

    # Draw button text
    screen.blit(button_text1, (button1.centerx - button_text1.get_width() // 2, button1.centery - button_text1.get_height() // 2))
    screen.blit(button_text2, (button2.centerx - button_text2.get_width() // 2, button2.centery - button_text2.get_height() // 2))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
