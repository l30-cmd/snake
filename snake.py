import random, time, threading, getkey

class GameStatus:           # defining and storing the game's status in a global class GameStatus. Otherwise the threats are coliding or only using local variables.
    def __init__(self, gridsize=10, speed=1.0):  # Added 'self' as the first parameter
        self.snake = [(3,0), (3,1), (3,2)]
        self.gridsize = gridsize
        self.speed = speed
        self.food = self.spawn_food()
        self.latest_key = 'd'
        self.running = True
        self.lock = threading.Lock()

        #print("What grid size do you want to use? Choose something between 5-30: ")      >>>>>>>> # Implement later on.
        #print("What speed do you want to play with? Choose something between 0.1 and 5: ")      >>>>>>>> # Implement later on.
    
    def spawn_food(self):  # Added 'self' as the first parameter
        while True:
            self.food = (random.randint(0, self.gridsize - 1), random.randint(0, self.gridsize - 1))
            if self.food not in self.snake:
                return self.food    
        
def print_grid(status):   # Modify print_grid to Show Food
    print("\n\n")
    grid = [['.' for _ in range(status.gridsize)] for _ in range(status.gridsize)]

    # Place the snake on the grid
    for x, y in status.snake:  # Changed 'self' to 'status'
        grid[x][y] = 'X'

    # Place the food
    fx, fy = status.food  # Changed 'self' to 'status'
    grid[fx][fy] = 'F' # Represent food with 'F'

    # Print the grid
    for row in grid:
        print(" ".join(row))
    
    print("\nWhich direction you wanna move? ( w / s / a / d ) or 'l' to leave the game: ")    

def move_snake_safe(status):  # Modify move_snake_safe to Grow Snake
    head_x, head_y = status.snake[-1]

    if status.latest_key == 'w':  # Up
        new_head = (head_x - 1, head_y)
    elif status.latest_key == 's':  # Down
        new_head = (head_x + 1, head_y)
    elif status.latest_key == 'd':  # Right
        new_head = (head_x, head_y + 1)
    elif status.latest_key == 'a':  # Left
        new_head = (head_x, head_y - 1)
    elif status.latest_key == 'l':
        return

    else:
        print("Invalid key! Use 'w', 's', 'a', or 'd'.")
        return
    # Check for boundaries
    if not (0 <= new_head[0] < status.gridsize and 0 <= new_head[1] < status.gridsize):
        print("Invalid move: Out of bounds!")
        return

    # Check for collisions
    if new_head in status.snake:
        print("Invalid move: Collision detected!")
        return

    # If the snake eats food, grow it (don't remove tail)
    if new_head == status.food:
        status.snake.append(new_head)
        status.food = status.spawn_food()   # Generate new food
    else:
        status.snake.append(new_head)
        status.snake.pop(0)               # Keep snake length the same

    return

def goodbye(status):
    print("\n\n ***  Slither Sisters thank you for playing.  ***\n\nYou are awesome no matter what!\n\n ***  Bye!  ***\n\n\n")
    status.running = False

def user_input(status):
    while status.running: # loop until "l" is pressed and self.running = False
        print_grid(status)
        status.latest_key = getkey.getkey() 

        if status.latest_key == "l":
            goodbye(status)
            status.running = False
            return # exiting the endless function and the game
   
        move_snake_safe(status)

def auto_move(status):
    while status.running:
        print_grid(status)
        time.sleep(0.5)
        move_snake_safe(status)

def starting_snake_game():  # Modify Game Loop to Handle Food
    status = GameStatus()    # handing all variables in the global class GameStatus.
    print("\n"*3, " ~~~   ***   The Pyladies\' Slither Sisters present.   ***   ~~~", "\n"*2)
    time.sleep(status.speed)
    print("Welcome to the Slither Sisters' version of Snake!\n")
    time.sleep(status.speed)
    print("Moving with the following keys:\n w... up \n s... down\n a... left\n d... right\n Pause with the Space key, continoue with a direction key.\n") 
    time.sleep(status.speed)

    threading.Thread(target=user_input, args = (status,)).start()  # user_input thread with all arguments packed into status 
    threading.Thread(target=auto_move, args = (status, )).start() 

starting_snake_game()   # Starting the game

exit()
quit()
