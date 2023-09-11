import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)  # Black
CIRCLE_RADIUS = 10
CIRCLE_FADE_SPEED = 0.15  # Increase in radius per frame
CIRCLE_ALPHA_FADE_SPEED = 1  # Decrease in alpha per frame

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click Highlighter")

# List to store the circle objects
circles = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle left mouse button click (white circle)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            circles.append({"x": mouse_x, "y": mouse_y, "radius": 0, "alpha": 255, "color": (255, 255, 255)})

        # Handle right mouse button click (light blue circle)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            circles.append({"x": mouse_x, "y": mouse_y, "radius": 0, "alpha": 255, "color": (173, 216, 230)})

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Create a list to store circles that need to be removed
    circles_to_remove = []

    # Draw and update circles
    for circle in circles:
        x, y, radius, alpha, color = circle["x"], circle["y"], circle["radius"], circle["alpha"], circle["color"]
        if alpha > 0:
            pygame.draw.circle(screen, (*color, alpha), (x, y), radius)
            circle["radius"] += CIRCLE_FADE_SPEED
            circle["alpha"] -= CIRCLE_ALPHA_FADE_SPEED
        else:
            circles_to_remove.append(circle)  # Add circles that have faded out

    # Remove circles that have faded completely
    for circle in circles_to_remove:
        circles.remove(circle)

    pygame.display.flip()
