import pygame
import random
import os

pygame.init()

# Set up the window
width = 800
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up game variables
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

score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

# Game modes
MODE_FRIEND = 0
MODE_AI = 1

game_mode = None
game_started = False

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file paths for the sound files
bounce_sound_path = os.path.join(current_dir, "bounce.wav")
score_sound_path = os.path.join(current_dir, "score.wav")

# Load the sound files
bounce_sound = pygame.mixer.Sound(bounce_sound_path)
score_sound = pygame.mixer.Sound(score_sound_path)

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not game_started:
                if event.key == pygame.K_1:
                    game_mode = MODE_FRIEND
                    game_started = True
                elif event.key == pygame.K_2:
                    game_mode = MODE_AI
                    game_started = True

    if not game_started:
        # Display the game menu
        win.fill(BLACK)

        title_text = font.render("Pong", True, WHITE)
        win.blit(title_text, (width // 2 - title_text.get_width() // 2, 100))

        mode_text = font.render("Select Game Mode:", True, WHITE)
        win.blit(mode_text, (width // 2 - mode_text.get_width() // 2, 200))

        friend_text = font.render("1. Play with a Friend", True, WHITE)
        win.blit(friend_text, (width // 2 - friend_text.get_width() // 2, 250))

        ai_text = font.render("2. Play with AI", True, WHITE)
        win.blit(ai_text, (width // 2 - ai_text.get_width() // 2, 300))

        pygame.display.update()
        continue

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < height - paddle_height:
        paddle1_y += paddle_speed

    if game_mode == MODE_FRIEND:
        # Player 2 controls the second paddle using arrow keys
        if keys[pygame.K_UP] and paddle2_y > 0:
            paddle2_y -= paddle_speed
        if keys[pygame.K_DOWN] and paddle2_y < height - paddle_height:
            paddle2_y += paddle_speed

    if game_mode == MODE_AI:
        # AI controls the second paddle
        if paddle2_y + paddle_height // 2 < ball_y:
            paddle2_y += paddle_speed
        if paddle2_y + paddle_height // 2 > ball_y:
            paddle2_y -= paddle_speed

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Handle ball collisions with paddles
    if ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_speed_x = abs(ball_speed_x)
        bounce_sound.play()
    if ball_x >= paddle2_x - ball_radius and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_speed_x = -abs(ball_speed_x)
        bounce_sound.play()

    # Handle ball collisions with walls
    if ball_y <= 0 or ball_y >= height - ball_radius:
        ball_speed_y = -ball_speed_y
        bounce_sound.play()

    # Handle ball scoring
    if ball_x < 0:
        score2 += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_speed_x = random.choice([3, -3])
        ball_speed_y = random.choice([3, -3])
        score_sound.play()
    if ball_x > width:
        score1 += 1
        ball_x = width // 2
        ball_y = height // 2
        ball_speed_x = random.choice([3, -3])
        ball_speed_y = random.choice([3, -3])
        score_sound.play()

    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(win, WHITE, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.circle(win, WHITE, (ball_x, ball_y), ball_radius)

    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    win.blit(score_text, (width // 2 - score_text.get_width() // 2, 10))

    pygame.display.update()

pygame.quit()