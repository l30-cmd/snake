import time
import getkey

# Create a function to make a blank grid (just dots)
def initial_grid(rows=10, cols=10):
    grid = [['.' for _ in range(cols)] for _ in range(rows)]
    return grid

# Include this 2nd function to visualise the blank grid
def print_grid(grid):
    for row in grid:
        print(' '.join(row))

# Choosing which level and HOW FAST the snake is going to be
# Function to be defined later on - in the testing phase the snake's speed is every 2 secounds.
t = 2 # 2 sec delay
print (t)

# Want to see what the previous 2 functions did.  Plus, personalise the presentation a bit.
grid = initial_grid()
print('\n ~~~   ***   The Pyladies\' Slither Sisters present.   ***   ~~~ \n')
time.sleep(t)
print("Welcome to the Slither Sisters' version of Snake!\n \n")
time.sleep(t)
print_grid(grid)
time.sleep(t)
print('\n \n \n')
time.sleep(t)
# Step 3 & 4: Interactive Movement Loop

def move_snake_safe(snake, key, grid_size=10):
    head_x, head_y = snake[-1]
    
    if key == 'w':  # north or up
        new_head = (head_x - 1, head_y)
    elif key == 's':    # south or down
        new_head = (head_x + 1, head_y)
    elif key == 'd':    # east or right
        new_head = (head_x, head_y + 1)
    elif key == 'a':    # west or left
        new_head = (head_x, head_y - 1)
    else:
        print("Invalid key! Use 'w', 's', 'a', or 'd' to move your snake.")  # "w", "a", "s", "d" for key, use
        return False  # Invalid key
    
    # Check if the new position is out of bounds
    if not (0 <= new_head[0] < grid_size and 0 <= new_head[1] < grid_size):
        print("Invalid move: Out of bounds!")
        return False
    
    # Check if the new position collides with the snake itself
    if new_head in snake:
        print("Invalid move: Collision detected!")
        return False
    
    snake.append(new_head)
    snake.pop(0)  # Maintain length
    time.sleep(1)
    print("\n \n \n *** ** * ** * ** *** \n \n \n")
    print_grid(snake, grid_size)
    print("\n \n \n")
    
    return True

def print_grid(snake, grid_size=10):
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    for x, y in snake:
        grid[x][y] = 'X'
    for row in grid:
        print(" ".join(row))

def interactive_snake_game():
    snake = [(0,0), (0,1), (0,2)]  # Initial snake position
    grid_size = 10
    
    while True:
        time.sleep(0.5)
        print_grid(snake, grid_size)
        
        while True:
            print("\n \n \n Which direction you wanna move?\n( w / a / s / d) or 'l' to leave the game: ")
            from getkey import getkey, keys
            key = getkey()
            
            if key == "l":
                break

            elif not move_snake_safe(snake, key, grid_size):
                print("Try a different move.")
    
    print("Game over! \n Slither Sisters thank you for playing.")
    time.sleep(1)
    print("You are awesome no matter what!\n")
    time.sleep(2)
    print(" ***  Bye!  ***")

# Run the interactive game
interactive_snake_game()
