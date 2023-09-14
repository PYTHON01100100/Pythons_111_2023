import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the paddles and ball
paddle_width = 10
paddle_height = 60
paddle_speed = 5
ball_radius = 10
ball_speed_x = 3
ball_speed_y = 3

paddle1_x = 50
paddle1_y = height // 2 - paddle_height // 2
paddle2_x = width - 50 - paddle_width
paddle2_y = height // 2 - paddle_height // 2
ball_x = width // 2
ball_y = height // 2

# Define the score variables
score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

# Define the AI paddle
ai_paddle_speed = 3

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # Limit the frame rate to 60 FPS

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the human-controlled paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < height - paddle_height:
        paddle1_y += paddle_speed

    # Move the AI paddle
    if paddle2_y + paddle_height // 2 < ball_y:
        paddle2_y += ai_paddle_speed
    if paddle2_y + paddle_height // 2 > ball_y:
        paddle2_y -= ai_paddle_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check collision with paddles
    if ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_speed_x = abs(ball_speed_x)  # Reverse the x-direction
    if ball_x >= paddle2_x - ball_radius and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_speed_x = -abs(ball_speed_x)  # Reverse the x-direction

    # Check collision with walls
    if ball_y <= 0 or ball_y >= height - ball_radius:
        ball_speed_y = -ball_speed_y  # Reverse the y-direction

    # Check if the ball is out of bounds
    if ball_x < 0:
        score2 += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_speed_x = random.choice([3, -3])
        ball_speed_y = random.choice([3, -3])
    if ball_x > width:
        score1 += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_speed_x = random.choice([3, -3])
        ball_speed_y = random.choice([3, -3])

    # Clear the screen
    win.fill(BLACK)

    # Draw the paddles and ball
    pygame.draw.rect(win, WHITE, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(win, WHITE, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.circle(win, WHITE, (ball_x, ball_y), ball_radius)

    # Draw the score
    score_text = font.render(str(score1) + " - " + str(score2), True, WHITE)
    win.blit(score_text, (width // 2 - score_text.get_width() // 2, 10))

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()