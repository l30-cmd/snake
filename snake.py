import random
#import turtle

import time #The other representation is a tuple of 9 integers giving local time. The tuple items are:   
#year (including century, e.g. 1998) month (1-12) day (1-31) hours (0-23) minutes (0-59) seconds (0-59) weekday (0-6, Monday is 0)

def field_setup():
    # seting up a board 10x10 with "."
    field = []
    field_s = str()
    yr = range(10)
    xr = range(10)

    for y in yr:
        for x in xr:
            field.append([y, x, "."])
            field_s = field_s + "."

            x = x + 1
        y = y + 1
        field_s = field_s + '\n'
    


    return(field, field_s)

def draw_map(field, snake_coord):
    # drawing the field with coordinates of the snake
    snake_x = snake_coord[0]
    snake_y = snake_coord[1]
    yr = range(10)
    xr = range(10)

    for y in yr:
        for x in xr:
            if (y, x) in snake_coord:
                field.append([y, x, '*'])
            else:
                field.append([y, x, "."])
                field_s = field_s + "."  

    # modifying an element in a sublist
    field[0][2] = '*'
    #print(field)

def snake_go():
    # moves snake per time strait forward
    pass

def field_refresh(x, y, input_key, s_length):
    # prints grid (with walls)
    # later: prints grid with snake
    pass


field = field_setup()
fieldcoord = field[0]
field_s = field[1]


print(field_s)
#for dots in board:
#    print(dots)
#print(board(range(10), [3]))
xm = range(10)
#ym = range(10)
#for yi in ym:
#for xi in xm:
#    print(board([xi][3])) 

coordi = [(0,0),(1,0),(2,0),(2,1),(2,1),(3,1)]
res2 = draw_map(fieldcoord, coordi)
