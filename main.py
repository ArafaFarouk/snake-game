import random 
import curses


# initialize the curses library to create the screen
screen = curses.initscr()
curses.curs_set(0)
screen_height, screen_width = screen.getmaxyx()

# create new window and  Set the dimensions of the playing screen
window = curses.newwin(screen_height, screen_width, 0 , 0)
window.keypad(1)
window.timeout(100)

# set coordinates the position of snake
snk_x = screen_width // 4
snk_y = screen_height // 2

# define the initial position of the snake body
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x -1],
    [snk_y, snk_x -2]
]

# create the food coordinates
food = [screen_height // 2, screen_width // 2]
# draw food on a screen 
window.addch(food[0], food[1], curses.ACS_PI)

# set initial movement direction to right 
key = curses.KEY_RIGHT

# create main game loop 
while True:
    # get the next key from user & create move 
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    """ if next_key == -1:
        key = key 
        else:
        key = next_key """
    # check if snake collided with the walls or itself 
    if snake[0][0] in [0, screen_height] or snake[0][1] in [0, screen_width] or snake[0] in snake[1]:
        curses.endwin()
        quit()

    # set the new position 
    new_head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWEN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    # insert the new head to the first position of snake list
    snake.insert(0,new_head)

    # check if snake ate the food 
    if snake[0] == food:
        food = None
        # create new food & set position x , y 
        while food is None:
            new_food = [
                random.randint(1, screen_height -1), # --> x new_food
                random.randint(1, screen_width -1), # --> y new_food 
            ]
            food = new_food if new_food not in snake else None 
        window.addch(food[0], food[1], curses.ACS_PI) 
    else:
        tall = snake.pop()
        window.addch(tall[0], tall[1], ' ') 
        
    # create snake in the window 
    window.addch(snake[0][0], snake[0][1], curses.ACS_BOARD)




