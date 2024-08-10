import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
CAR_SIZE = 50
OBSTACLE_SIZE = 50
TRACK_WIDTH = 200
TRACK_HEIGHT = HEIGHT - 100
FPS = 60

# Set up some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the clock
clock = pygame.time.Clock()

# Set up the car
car_x, car_y = WIDTH / 2, HEIGHT - CAR_SIZE * 2
car_speed = 5

# Set up the obstacles
obstacles = []
obstacle_speed = 3

# Set up the score
score = 0

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= car_speed
    if keys[pygame.K_RIGHT]:
        car_x += car_speed

    # Keep the car on the track
    if car_x < WIDTH / 2 - TRACK_WIDTH / 2:
        car_x = WIDTH / 2 - TRACK_WIDTH / 2
    elif car_x > WIDTH / 2 + TRACK_WIDTH / 2 - CAR_SIZE:
        car_x = WIDTH / 2 + TRACK_WIDTH / 2 - CAR_SIZE

    # Move the obstacles
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        if obstacle[1] > HEIGHT:
            obstacles.remove(obstacle)

    # Add new obstacles
    if random.random() < 0.05:
        obstacles.append([random.randint(WIDTH / 2 - TRACK_WIDTH / 2, WIDTH / 2 + TRACK_WIDTH / 2 - OBSTACLE_SIZE), -OBSTACLE_SIZE])

    # Check for collisions
    for obstacle in obstacles:
        if (obstacle[0] < car_x + CAR_SIZE and
            obstacle[0] + OBSTACLE_SIZE > car_x and
            obstacle[1] < car_y + CAR_SIZE and
            obstacle[1] + OBSTACLE_SIZE > car_y):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Update the score
    score += 1 / FPS

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (WIDTH / 2 - TRACK_WIDTH / 2, 0, TRACK_WIDTH, TRACK_HEIGHT))
    pygame.draw.rect(screen, RED, (car_x, car_y, CAR_SIZE, CAR_SIZE))
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], OBSTACLE_SIZE, OBSTACLE_SIZE))
    text = font.render(f"Score: {int(score)}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)