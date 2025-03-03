import pygame

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED_X, BALL_SPEED_Y = 4, 4
PADDLE_SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Paddle and Ball
paddle_width, paddle_height = 10, 100
ball_size = 10

# Positions
paddle1 = pygame.Rect(30, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)
paddle2 = pygame.Rect(WIDTH-40, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)
ball = pygame.Rect(WIDTH//2 - ball_size//2, HEIGHT//2 - ball_size//2, ball_size, ball_size)

# Ball direction
ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += PADDLE_SPEED

    # Ball Movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with top/bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # Ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_dx *= -1  # Reverse direction

    # Ball goes out of bounds (reset position)
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x, ball.y = WIDTH//2 - ball_size//2, HEIGHT//2 - ball_size//2
        ball_dx *= -1  # Restart direction

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))  # Middle line

    pygame.display.flip()
    clock.tick(60)  # Limit frame rate

pygame.quit()