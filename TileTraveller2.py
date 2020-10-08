# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

# Coin counter
coin_counter = 0

# Has a lever been pulled on this tile? T/F
duplicate_lever_pull = False

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def play_one_move(col, row, valid_directions):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row 
        Also return if tile has been checked for a lever'''
    victory = False
    direction = input("Direction: ")
    direction = direction.lower()
    
    if not direction in valid_directions:
        print("Not a valid direction!")
        duplicate_lever_pull = True
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        duplicate_lever_pull = False
    return victory, col, row, duplicate_lever_pull

def find_lever(col, row):
    ''' Returns True or False if there is a lever given the supplied location '''
    lever = False
    if col == 1 and row == 2: # (1,2)
        lever = True
    elif col == 2 and row == 2: # (2,2)
        lever = True
    elif col == 2 and row == 3: # (2,3)
        lever = True
    elif col == 3 and row == 2: # (3,2)
        lever = True
    return lever

def pull_lever(lever, counter):
    ''' If there is a lever on the tile it asks if you want to open it and if you open it you get a coin
    returns the value of the coin counter '''
    if lever:
        pull = input('Pull a lever (y/n): ')
        pull.lower()
        if pull == 'y':
            counter += 1
            print('You received 1 coin, your total is now {}.'.format(counter))
    return counter



# The main program starts here
victory = False
row = 1
col = 1

while not victory:
    if duplicate_lever_pull == False:
        lever = find_lever(col, row)
        coin_counter = pull_lever(lever, coin_counter)
    valid_directions = find_directions(col, row)
    print_directions(valid_directions)
    victory, col, row, duplicate_lever_pull = play_one_move(col, row, valid_directions)
print("Victory! Total coins {}.".format(coin_counter))