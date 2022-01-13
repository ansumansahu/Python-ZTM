#Generate a random number between range given by the user and keep guessing
#until we get the correct guess
#Use sys.argv to run the program by provinding input in termial itself

from math import e
import sys
import random
start=int(sys.argv[1])
end=int(sys.argv[2])

answer=random.randint(start,end)

guess=int(input(f'Guess a number between {start}-{end}: '))
number_of_guess=1
already_guessed=[]
while guess not in already_guessed and 0<guess<end+1:
    if guess==answer:
        print(f'Correct Answer in {number_of_guess} guesses')
        break
    already_guessed.append(guess)
    guess=int(input(f'Guess a number between {start}-{end}: '))
    number_of_guess+=1

# print(f'Guesses before getting the answer: {already_guessed}')
# To run type the following in terminal with directory same as file directory
# python .\guessing_game.py 1 10

# ---------------------------------------------------------------------------------------------------
# Below is the solution by instructor (it's better so i copied it for reference)

# from random import randint
# # you will need to run this on your machine and not this website for the sys.argv to work!
# import sys

# answer = randint(int(sys.argv[1]), int(sys.argv[2]))

# while True:
#     try:
#         guess = int(input(f'guess a number {sys.argv[1]}-{sys.argv[2]}:  '))
#         if  0 < guess < 6:
#             if guess == answer:
#                 print('you are a genius!')
#                 break
#         else:
#             print('Hey, I said between 1-6')
#     except ValueError:
#         print('please enter a number')
#         continue
