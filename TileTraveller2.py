import random

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

YES = 'y'
NO = 'n'

LEVER_LOCATIONS = [(1,2), (2,2), (2,3), (3,2)]

# Choice lists
direction_list = [NORTH, EAST, SOUTH, WEST]
yesno_list = [YES, NO]

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

def play_one_move(col, row, valid_directions, coin_counter, lever, move_counter):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row 
        Also return if tile has been checked for a lever'''
    victory = False
    move_counter += 1
    direction = random.choice(direction_list)
    print("Direction: {}".format(direction))
    
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        coin_counter = pull_lever(lever, coin_counter)
    return victory, col, row, coin_counter, move_counter

def find_lever(col, row, LEVER_LOCATIONS):
    ''' Returns True or False if there is a lever given the supplied location '''
    lever = False
    if (col, row) in LEVER_LOCATIONS:
        lever = True
    return lever

def pull_lever(lever, counter):
    ''' If there is a lever on the tile it asks if you want to open it and if you open it you get a coin
    returns the value of the coin counter '''
    if lever:
        pull = random.choice(yesno_list)
        print('Pull a lever (y/n): {}'.format(pull))
        if pull == YES:
            counter += 1
            print('You received 1 coin, your total is now {}.'.format(counter))
    return counter

def play(victory, row, col, coin_counter, move_counter, LEVER_LOCATIONS):
    seed = int(input('Input seed: '))
    random.seed(seed)
    while not victory:
        lever = find_lever(col, row, LEVER_LOCATIONS)
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row, coin_counter, move_counter = play_one_move(col, row, valid_directions, coin_counter, lever, move_counter)
    print("Victory! Total coins {}. Moves {}.".format(coin_counter, move_counter))
    play_again = input("Play again (y/n): ")
    play_again.lower()
    return play_again

# The main program starts here

play_again = YES

while play_again == YES:
    victory = False
    row = 1
    col = 1
    coin_counter = 0
    move_counter = 0
    play_again = play(victory, row, col, coin_counter, move_counter, LEVER_LOCATIONS)