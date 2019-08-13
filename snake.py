import pygame
import time
import random

pygame.init()

# *** BOARD DISPLAY SETTINGS
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

# *** COLORS
block_color = (255, 255, 255)
black = (0, 0, 0)
foodCol = (52, 155, 255)

# *** FONT
font = pygame.font.SysFont(None, 25)


def score(count):
    text = font.render("Score : "+str(count), True, block_color)

    with open('scores.txt', 'r') as f:
        for line in f:
            hs = font.render("Highscore: "+str(line), True, block_color)
            gameDisplay.blit(hs, (700, 0))

    gameDisplay.blit(text, (0, 0))


def snake(block_size, snakelist):
    # *** DRAWS THE SNAKE
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, block_color, [
                         XnY[0], XnY[1], block_size, block_size])


def food(x, y):
    pygame.draw.rect(gameDisplay, foodCol, [x, y, 10, 10])


def message_to_screen(msg, color):
    # *** DISPLAY THE DIED TEXT ON THE SCREEN
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    pygame.quit()
    quit()


def start_game():

    x_change = 0
    y_change = 0

    snakeList = []

    # *** THE SNAKE SIZE (WIDTH, HEIGHT)
    snake_size = 10

    # *** DEFAULT POSISTION OF THE SNAKE
    snake_x_pos = display_width/2
    snake_y_pos = display_height/2

    snakeLength = 1
    endGame = False

    # *** FOOD'S POSITION IN THE SCREEN
    # *** GENERATE A RANDOM POSITION WITHIN THE SCREEN
    food_x = round(random.randrange(0, display_width-10)/10.0)*10.0
    food_y = round(random.randrange(0, display_height-10)/10.0)*10.0

    while not endGame:
        # *** GET ALL THE EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                message_to_screen('You died', foodCol)
                endGame = True

            # *** CHECK FOR THE ARROW KEY EVENTS
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    y_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                    y_change = 0
                if event.key == pygame.K_UP:
                    y_change = -5
                    x_change = 0
                if event.key == pygame.K_DOWN:
                    y_change = 5
                    x_change = 0

        # *** ADD THE SNAKE'S MOVEMENT IN THE X,Y AXIS
        snake_y_pos += y_change
        snake_x_pos += x_change

        gameDisplay.fill(black)
        food(food_x, food_y)

        # *** IF THE SNAKE GOES FROM THE X AXIS (LEFT , RIGHT)
        # *** START BACK
        if snake_x_pos > display_width:
            snake_x_pos = 0
        elif snake_x_pos + display_width < display_width:
            snake_x_pos = display_width

        # *** IF THE SNAKE GOES FROM THE Y AXIS (TOP , BOTTOM)
        # *** START BACK
        if snake_y_pos > display_height:
            snake_y_pos = 0
        elif snake_y_pos + display_height < display_height:
            snake_y_pos = display_height

        # *** ADD THE SNAKE HEAD TO THE LIST ***
        # *** EVERYTIME IT EATS ***
        snakeHead = []
        snakeHead.append(snake_x_pos)
        snakeHead.append(snake_y_pos)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        # *** CHECK IF YOU BIT YOURSELF ***
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                print('Died\n')
                message_to_screen('You died', foodCol)

        # *** Draw the snakes ***
        snake(snake_size, snakeList)

        # *** UPDATE THE SCREEN ***
        pygame.display.update()
        if food_x == snake_x_pos and food_y == snake_y_pos:
            food_x = round(random.randrange(0, display_width-10)/10.0)*10.0
            food_y = round(random.randrange(
                0, display_height-10)/10.0)*10.0
            print('nom nom')
            snakeLength += 1
            text = font.render("Score : "+str(snakeLength), True, foodCol)
            gameDisplay.blit(text, (0, 0))

        clock.tick(60)


start_game()


pygame.quit()
quit()
