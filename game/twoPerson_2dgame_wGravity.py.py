import pygame
pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
ORANGE=(255,140,0)
BLUE = (4,217,255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CHAR_WIDTH = 50
CHAR_HEIGHT = 50
CHAR_SPEED = 4
CHAR_SPEED1 = 15
BULLET_SPEED = 10
BULLET_RADIUS = 5

DECELERATION_FACTOR = 0.2

font = pygame.font.Font(None, 36)

# Set up the health values for both characters
player1_health = 100
player2_health = 100

# Set up the health bar dimensions
health_bar_length = 200
health_bar_height = 20
import math

def ai_move():
    global x2, y2, x_vel2, y_vel2

    # Calculate the distance between the AI character and the player character
    dist_x = x1 - x2
    dist_y = y1 - y2
    dist = math.sqrt(dist_x**2 + dist_y**2)

    # If the player is within a certain range, move towards them
    if dist < 200:
        if dist_x > 0:
            x_vel2 = CHAR_SPEED
        elif dist_x < 0:
            x_vel2 = -CHAR_SPEED
        else:
            x_vel2 = 0

        if dist_y > 0:
            y_vel2 = CHAR_SPEED
        elif dist_y < 0:
            y_vel2 = -CHAR_SPEED
        else:
            y_vel2 = 0

    # Otherwise, move randomly
    else:
        x_vel2 += random.choice([-1, 1]) * CHAR_SPEED
        y_vel2 += random.choice([-1, 1]) * CHAR_SPEED

    # Apply deceleration
    if x_vel2 > 0:
        x_vel2 = max(x_vel2 - DECELERATION_FACTOR, 0)
    elif x_vel2 < 0:
        x_vel2 = min(x_vel2 + DECELERATION_FACTOR, 0)

    if y_vel2 > 0:
        y_vel2 = max(y_vel2 - DECELERATION_FACTOR, 0)
    elif y_vel2 < 0:
        y_vel2 = min(y_vel2 + DECELERATION_FACTOR, 0)

    # Update the position of the AI character
    x2 += x_vel2
    y2 += y_vel2

    # Make sure the AI character stays within the screen bounds
    if x2 < 0:
        x2 = 0
    elif x2 + CHAR_WIDTH > SCREEN_WIDTH:
        x2 = SCREEN_WIDTH - CHAR_WIDTH

    if y2 < 0:
        y2 = 0
    elif y2 + CHAR_HEIGHT > SCREEN_HEIGHT:
        y2 = SCREEN_HEIGHT - CHAR_HEIGHT

# Define the function to draw the health bars
def draw_health_bars():
    # Draw the player 1 health bar
    pygame.draw.rect(screen, WHITE, (10, 10, health_bar_length, health_bar_height))
    pygame.draw.rect(screen, ORANGE, (10, 10, player1_health * 2, health_bar_height))

    # Draw the player 2 health bar
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - health_bar_length - 10, 10, health_bar_length, health_bar_height))
    pygame.draw.rect(screen, GREEN, (SCREEN_WIDTH - player2_health * 2 - 10, 10, player2_health * 2, health_bar_height))

    # Add text to the health bars
    player1_text = font.render("Yilmaz", True, WHITE)
    player2_text = font.render("CiciKus", True, WHITE)
    screen.blit(player1_text, (10, 35))
    screen.blit(player2_text, (SCREEN_WIDTH - health_bar_length - 10, 35))
character1 = pygame.image.load("images/character.png")

character2 = pygame.image.load("images/character2.png")

yilmaz_yorgun=pygame.image.load("images/yilmaz_yorgun.png")
cicikus_yorgun=pygame.image.load("images/cicikus_yorgun.png")

background = pygame.image.load("images/background.jpg")

background = pygame.transform.smoothscale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Character Movement")

clock = pygame.time.Clock()

x1 = SCREEN_WIDTH // 4 - CHAR_WIDTH // 2

y1 = SCREEN_HEIGHT // 2 - CHAR_HEIGHT // 2

x_vel1 = 0

y_vel1 = 0

x2 = SCREEN_WIDTH * 3 // 4 - CHAR_WIDTH // 2

y2 = SCREEN_HEIGHT // 2 - CHAR_HEIGHT // 2

x_vel2 = 0

y_vel2 = 0

bullets = []
bullets2 = []

# In the main loop, handle the SHOOT event
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                x_vel1 = -CHAR_SPEED1

            if event.key == pygame.K_RIGHT :
                x_vel1 = CHAR_SPEED1

            if event.key == pygame.K_UP :
                y_vel1 = -CHAR_SPEED1

            if event.key == pygame.K_DOWN:
                y_vel1 = CHAR_SPEED1

            if event.key == pygame.K_a:
                x_vel2 = -CHAR_SPEED

            if event.key == pygame.K_d:
                x_vel2 = CHAR_SPEED

            if event.key == pygame.K_w:
                y_vel2 = -CHAR_SPEED

            if event.key == pygame.K_s:
                y_vel2 = CHAR_SPEED

            if event.key == pygame.K_SPACE:

                if x_vel1 < 0:
                    bullet = {"x": x1, "y": y1 + CHAR_HEIGHT // 2, "vx": -BULLET_SPEED, "vy": 0}
                elif x_vel1 > 0:
                    bullet = {"x": x1 + CHAR_WIDTH, "y": y1 + CHAR_HEIGHT // 2, "vx": BULLET_SPEED, "vy": 0}
                elif y_vel1 < 0:
                    bullet = {"x": x1 + CHAR_WIDTH // 2, "y": y1, "vx": 0, "vy": -BULLET_SPEED}
                else:
                    bullet = {"x": x1 + CHAR_WIDTH, "y": y1 + CHAR_HEIGHT // 2, "vx": BULLET_SPEED, "vy": 0}

                # Add the bullet to the list of bullets
                bullets.append(bullet)

            if event.key == pygame.K_LCTRL:
                # Set the velocity of the bullet based on the direction the character is facing
                if x_vel2 < 0:
                    bullet2 = {"x": x2, "y": y2 + CHAR_HEIGHT // 2, "vx": -BULLET_SPEED, "vy": 0}
                elif x_vel2 > 0:
                    bullet2 = {"x": x2 + CHAR_WIDTH, "y": y2 + CHAR_HEIGHT // 2, "vx": BULLET_SPEED, "vy": 0}
                elif y_vel2 < 0:
                    bullet2 = {"x": x2 + CHAR_WIDTH // 2, "y": y2, "vx": 0, "vy": -BULLET_SPEED}
                else:
                    bullet2 = {"x": x2, "y": y2 + CHAR_HEIGHT // 2, "vx": -BULLET_SPEED, "vy": 0}
                # Add the bullet to the list of bullets
                bullets2.append(bullet2)

        if event.type == pygame.KEYUP:
          
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                x_vel1 = 0

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                y_vel1 = 0

            if event.key == pygame.K_a and x_vel2 < 0:
                x_vel2 += DECELERATION_FACTOR * CHAR_SPEED
            if event.key == pygame.K_d and x_vel2 > 0:
                x_vel2 -= DECELERATION_FACTOR * CHAR_SPEED
            if event.key == pygame.K_w and y_vel2 < 0:
                y_vel2 += DECELERATION_FACTOR * CHAR_SPEED
            if event.key == pygame.K_s and y_vel2 > 0:
                y_vel2 -= DECELERATION_FACTOR * CHAR_SPEED

  

    x1 += x_vel1
    y1 += y_vel1
    x2 += x_vel2
    y2 += y_vel2
    if x1 < 0:
        x1 = 0
    elif x1 > SCREEN_WIDTH - CHAR_WIDTH:
        x1 = SCREEN_WIDTH - CHAR_WIDTH

    if y1 < 0:
        y1 = 0
    elif y1 > SCREEN_HEIGHT - CHAR_HEIGHT:
        y1 = SCREEN_HEIGHT - CHAR_HEIGHT

    if x2 < 0:
        x2 = 0
    elif x2 > SCREEN_WIDTH - CHAR_WIDTH:
        x2 = SCREEN_WIDTH - CHAR_WIDTH

    if y2 < 0:
        y2 = 0
    elif y2 > SCREEN_HEIGHT - CHAR_HEIGHT:
        y2 = SCREEN_HEIGHT - CHAR_HEIGHT
    if x_vel1 < 0:
        x_vel1 = max(x_vel1, -CHAR_SPEED)
    elif x_vel1 > 0:
        x_vel1 = min(x_vel1, CHAR_SPEED)
    if y_vel1 < 0:
        y_vel1 = max(y_vel1, -CHAR_SPEED)
    elif y_vel1 > 0:
        y_vel1 = min(y_vel1, CHAR_SPEED)

    if x_vel2 < 0:
        x_vel2 = max(x_vel2, -CHAR_SPEED)
    elif x_vel2 > 0:
        x_vel2 = min(x_vel2, CHAR_SPEED)
    if y_vel2 < 0:
        y_vel2 = max(y_vel2, -CHAR_SPEED)
    elif y_vel2 > 0:
        y_vel2 = min(y_vel2, CHAR_SPEED)

    # for bullet in bullets:
    #     bullet['x'] += bullet['vx']
    #     bullet['y'] += bullet['vy']

    # for bullet2 in bullets2:
    #     bullet2['x'] += bullet2['vx']
    #     bullet2['y'] += bullet2['vy']
# In the main loop, move the bullets and check for collisions
    for bullet in bullets:
        bullet["x"] += bullet["vx"]
        bullet["y"] += bullet["vy"]
        if bullet["x"] < 0 or bullet["x"] > SCREEN_WIDTH or bullet["y"] < 0 or bullet["y"] > SCREEN_HEIGHT:
            # Remove the bullet if it goes off the screen
            bullets.remove(bullet)
        elif x1 < bullet["x"] < x1 + CHAR_WIDTH and y1 < bullet["y"] < y1 + CHAR_HEIGHT:
            # Remove the bullet and deduct health from character1 if it hits character1
            bullets.remove(bullet)
            # Deduct health from character1
        elif x2 < bullet["x"] < x2 + CHAR_WIDTH and y2 < bullet["y"] < y2 + CHAR_HEIGHT:
            # Remove the bullet and deduct health from character2 if it hits character2
            bullets.remove(bullet)
            # Deduct health from character2

    for bullet in bullets2:
        bullet["x"] += bullet["vx"]
        bullet["y"] += bullet["vy"]
        if bullet["x"] < 0 or bullet["x"] > SCREEN_WIDTH or bullet["y"] < 0 or bullet["y"] > SCREEN_HEIGHT:
            # Remove the bullet if it goes off the screen
            bullets2.remove(bullet)
        elif x1 < bullet["x"] < x1 + CHAR_WIDTH and y1 < bullet["y"] < y1 + CHAR_HEIGHT:
            # Remove the bullet and deduct health from character1 if it hits character1
            bullets2.remove(bullet)
            # Deduct health from character1
        elif x2 < bullet["x"] < x2 + CHAR_WIDTH and y2 < bullet["y"] < y2 + CHAR_HEIGHT:
            # Remove the bullet and deduct health from character2 if it hits character2
            bullets2.remove(bullet)
            # Deduct health from character2

    # In the main loop, draw the bullets on the screen

    # player1_health -= 1
    # player2_health -= 2

    # Clear the screen
    # screen.fill((0, 0, 0))

    # Draw the health bars
   

    # Update the display
    # pygame.display.update()
    # Remove any bullets that have gone off the screen or hit something
    bullets = [bullet for bullet in bullets if bullet['y'] > -BULLET_RADIUS and 0 < bullet['x'] < SCREEN_WIDTH]

    bullets2 = [bullet for bullet in bullets2 if bullet['y'] > -BULLET_RADIUS and 0 < bullet['x'] < SCREEN_WIDTH]

    screen.blit(background, (0, 0))

    # Draw the first character on the screen at its position
    screen.blit(character1, (x1, y1))

    # Draw the second character on the screen at its position
    screen.blit(character2, (x2, y2))
#     for bullet in bullets:
#             pygame.draw.circle(screen, RED, (bullet['x'], bullet['y']), BULLET_RADIUS)

#     for bullet in bullets2:
#         pygame.draw.circle(screen, BLUE, (bullet['x'], bullet['y']), BULLET_RADIUS)
# # Update the display
 # Check for collisions between character 1 and bullets fired by character 2
    for bullet in bullets2:
        bullet_rect = pygame.Rect(bullet["x"] - BULLET_RADIUS, bullet["y"] - BULLET_RADIUS,
                                BULLET_RADIUS * 2, BULLET_RADIUS * 2)
        pygame.draw.circle(screen, BLUE, (bullet["x"], bullet["y"]), BULLET_RADIUS)

        if bullet_rect.colliderect(pygame.Rect(x1, y1, CHAR_WIDTH, CHAR_HEIGHT)):
            print("Character 1 hit by bullet!")
            if(player1_health<=0):
                print("Char DEAD")
                background = pygame.transform.smoothscale(yilmaz_yorgun, (SCREEN_WIDTH, SCREEN_HEIGHT))

            player1_health -=10

    # Check for collisions between character 2 and bullets fired by character 1
    for bullet in bullets:
        bullet_rect = pygame.Rect(bullet["x"] - BULLET_RADIUS, bullet["y"] - BULLET_RADIUS,
                                BULLET_RADIUS * 2, BULLET_RADIUS * 2)
        pygame.draw.circle(screen, RED, (bullet["x"], bullet["y"]), BULLET_RADIUS)

        if bullet_rect.colliderect(pygame.Rect(x2, y2, CHAR_WIDTH, CHAR_HEIGHT)):
            print("Character 2 hit by bullet!")
            if(player2_health<=0):
                background = pygame.transform.smoothscale(cicikus_yorgun, (SCREEN_WIDTH, SCREEN_HEIGHT))

                print("Char DEAD")

            player2_health-=10
    draw_health_bars()
    pygame.display.update()

    clock.tick(60)

# Quit pygame
pygame.quit()