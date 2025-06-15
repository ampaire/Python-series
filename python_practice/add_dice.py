
"""
This program simulates the rolling of two dice and prints the result of their sum on each roll.
"""

import random
def main():
    #number of sides on each die
    num_sides = 6

    #setup each die 
    die1 = random.randint(1, num_sides)
    die2 = random.randint(1, num_sides)

    #sum of each roll of the dice
    sum_of_dice = die1 + die2
    print(f'You rolled two dice each with {num_sides} sides.')
    print(f'The first die rolled a {die1}.')
    print(f'The second die rolled a {die2}.')
    print(f'The sum of the two dice is {sum_of_dice}.')

if __name__ == "__main__":
    main()
