import math
import random

# "¤" is marked as hit
# "o" is mark for miss
# "~" is mark for water

# ooooooooooooooooooooooooooooooooooooooo
# Global variables and constants

Random_Ship_Placer = [['~'] * 5 for x in range(5)]
Play__ground = [['~'] * 5 for x in range(5)]

guesses_left = 6

abc_to_123_ = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4
    }

_123_to_abc = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e'
    }

abc_strin = ["a", "b", "c", "d", "e"]

# ooooooooooooooooooooooooooooo

# ooooo functions oooooo


def board_(board):
    """Create a 5 x 5 matrix for"""
    row_number = 1
    for row in board:
        rowprint = [" | ", " | ", " | ", " | ", " | "]
        itx = 0
        for i in row:
            if '¤' in i:
                rowprint[itx] = "¤|"
            else:
                rowprint[itx] = " |"
            itx += 1
        long_line = rowprint[0]+rowprint[1]+rowprint[2]+rowprint[3]+rowprint[4]
        print(row_number, long_line)
        row_number += 1


def random_placer(board):
    """ Create ships in unique slots Random_Ship_Placer """
    for ship in range(4):
        row_placer = random.randint(0, 4)
        column_placer = random.randint(0, 4)
        while board[row_placer][column_placer] == '¤':
            row_placer = random.randint(0, 4)
            column_placer = random.randint(0, 4)
        board[row_placer][column_placer] = '¤'


def enter_value_playground():
    """calls inputs for validate. """
    row = input("Enter a number between 1   <-> 5:\n")
    while len(row) == 0:
        row = input("Enter a number between 1   <-> 5:\n")
    while abs(int(row)) > 5:
        row = input("You need to enter a number between 1   <-> 5:\n")
    # [bug fix] input can not be a int and a string
    if row not in '12345':
        print("enter a valid row")
        row = input("enter a row in letter a  <-> e:\n")
    column = input('enter letter a  <-> e:\n').lower()
    while column not in abc_strin:
        print('enter a valid column')
        column = input('enter a ship column a  <-> e:\n').lower()
    return int(row)-1, abc_to_123_[column]


def score(board):
    counter = 0
    for row in board:
        for column in row:
            if column == '¤':
                counter += 1


random_placer(Random_Ship_Placer)


def fight(guesses_left):
    print("welcome")
    while guesses_left > 0:
        print('.......')
        for i in Play__ground:
            print('|'+i[0]+i[1]+i[2]+i[3]+i[4]+'|')
        print('´´´´´´´')
        row, column = enter_value_playground()

        print_letter = _123_to_abc[column]

        if Play__ground[row][column] == 'o':
            print(f"{row+1} & {print_letter} is not unique, tye again")
        elif Random_Ship_Placer[row][column] == '¤':
            print(f"{row+1} & {print_letter} was a hit ")
            Play__ground[row][column] = '¤'
            guesses_left -= 1
        else:
            print(f'{row+1} & {print_letter} you missed')
            Play__ground[row][column] = 'o'
            guesses_left -= 1
        if score(Play__ground) == 5:
            print("congrats you have done the Unthinkable")
            break
        print (f'{guesses_left} guesses_left left')
        if guesses_left == 0:
            print("game over")
            break

# oooooooooooooooooooooooooooooooooooooooooooo
    """when guesses_left is zero board will print:"""
    board_(Random_Ship_Placer)  # where random ships where.
    print('------------')
    board_(Play__ground)        # if a guessed place was a hit.
    print('------------')
    print('Thank you for playing battleships.')


fight(guesses_left)
""" The game """
