from random import *
import sys

word_list = ['inquisitive', 'energetic', 'energetic', 'watery', 'amuck', 'superb', 'high', 'board', 'general', 'probably', 'island', 'giants', 'paper', 'income', 'spiritual', 'squash', 'uttermost' 'yam', 'marked', 'gorgeous', 'dog', 'sister', 'impulse', 'quicksand', 'momentous', 'discussion']

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def required_image(wrong_guess_num):
    if wrong_guess_num <= 0:
        print("""

   IIIIIIIIIIIII
   I           |
   I           |
   I           |
   I           |
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
 __I_______________________
[UUUUUUUUUUUUUUUUUUUUUUUUUU]
    """)


    elif wrong_guess_num == 1:
        print("""

   IIIIIIIIIIIII
   I           |
   I           |
   I           |
   I           |
   I         NNNNN
   I        N     N
   I       N  O O  N
   I       N   u   N
   I        NN   NN
   I           N
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
 __I_______________________
[UUUUUUUUUUUUUUUUUUUUUUUUUU]
    """)

    elif wrong_guess_num == 2:
        print("""

   IIIIIIIIIIIII
   I           |
   I           |
   I           |
   I           |
   I         NNNNN
   I        N     N
   I       N  O O  N
   I       N   u   N
   I        NN   NN
   I           N
   I        NNNNNNN
   I         NNNNN
   I          NNN
   I           N
   I           N
   I
   I
   I
   I
   I
   I
   I
   I
   I
   I
 __I_______________________
[UUUUUUUUUUUUUUUUUUUUUUUUUU]
    """)

    elif wrong_guess_num == 3:
        print("""

   IIIIIIIIIIIII
   I           |
   I           |
   I           |
   I           |
   I         NNNNN
   I        N     N
   I       N  O O  N
   I       N   _   N
   I        NN   NN
   I           N
   I        NNNNNNN
   I       N NNNNN
   I      N   NNN
   I      N    N
   I      N    N
   I           N
   I           N
   I
   I
   I
   I
   I
   I
   I
   I
 __I_______________________
[UUUUUUUUUUUUUUUUUUUUUUUUUU]
    """)

    elif wrong_guess_num == 4:
        print("""

   IIIIIIIIIIIII
   I           |
   I           |
   I           |
   I           |
   I         NNNNN
   I        N     N
   I       N  o o  N
   I       N   _   N
   I        NN   NN
   I           N
   I        NNNNNNN
   I       N NNNNN N
   I      N   NNN   N
   I      N    N    N
   I      N    N    N
   I           N
   I           N
   I
   I
   I
   I
   I
   I
   I
   I
 __I_______________________
[UUUUUUUUUUUUUUUUUUUUUUUUUU]
    """)

    elif wrong_guess_num == 5:
        print("""

   IIIIIIIIIIIII
   I           |
   I           |
   I           |
   I           |
   I         NNNNN
   I        N     N
   I       N  o o  N
   I       N   n   N
   I        NN   NN
   I           N
   I        NNNNNNN
   I       N NNNNN N
   I      N   NNN   N
   I      N    N    N
   I      N    N    N
   I           N
   I           NN
   I             N
   I             N
   I             N
   I             NNN
   I
   I
   I
   I
 __I_______________________
[UUUUUUUUUUUUUUUUUUUUUUUUUU]
    """)

    elif wrong_guess_num == 6:
        print("""

   IIIIIIIIIIIII
   I           |
   I           |
   I           |
   I           |
   I         NNNNN
   I        N \ / N
   I       N  X X  N
   I       N   n   N
   I        NN   NN
   I           N
   I        NNNNNNN
   I       N NNNNN N
   I      N   NNN   N
   I      N    N    N
   I      N    N    N
   I           N
   I          NNN
   I         N   N
   I         N   N
   I         N   N
   I       NNN   NNN
   I
   I
   I
   I
 __I_______________________
[UUUUUUUUUUUUUUUUUUUUUUUUUU]
    """)

    elif wrong_guess_num == 1024:
        print("""
   IIIIIIIIIIIII
   I           |
   I           |
   I           |
   I           |
   I
   I
   I
   I
   I
   I         NNNNN
   I     M  N     N  M
   I     N N  O O  N N
   I     N N   o   N N
   I      N NN   NN N
   I       N   N   N
   I        NNNNNNN
   I         NNNNN
   I          NNN
   I           N
   I           N
   I           N
   I          NNN
   I         N   N
   I         N   N
   I         N   N
 __I_______NNN   NNN_______
[UUUUUUUUUUUUUUUUUUUUUUUUUU]
        """)

def hangman_game():
    wrong_guess_num = 0
#    game_word = 'apple'
    game_word = word_list[randint(0, 24)]
    if len(game_word) > 5:
        wrong_guess_num -= 3
    game_list = list(game_word)
    guessed_letters = []
    hidden_list = []
    for i in game_list:
        hidden_list.append('?')
    hidden_word = ''.join(hidden_list)
    while (wrong_guess_num < 6) and (game_list != hidden_list):
        required_image(wrong_guess_num)
        hidden_word = ''.join(hidden_list)
        print("Here's your word ---> " + hidden_word)
        print("Here's what you've guessed so far: " + str(guessed_letters))
        print("Guess a letter.")
        entry = input()
        if entry not in game_list:
            wrong_guess_num += 1
            guessed_letters.append(entry)
            for i in range(len(game_word)):
                if game_list[i] == entry:
                    hidden_list[i] = game_list[i]
        elif entry in game_list:
            guessed_letters.append(entry)
#here starting letter replacer
            location_list = []
            for i in range(len(game_list)):
                if game_list[i] == entry:
                    location_list.append(i)
            for i in location_list:
                hidden_list[i] = entry
    if (wrong_guess_num) == 6 and (game_list != hidden_list):
        required_image(wrong_guess_num)
        print("You lose. >:( Your word was " + str(game_word) + ".")
        print("Would you like to play again?")
        again = input()
        if again.lower().startswith("y"):
            print("Here we go!")
            hangman_game()
        elif again.lower().startswith("n"):
            print("I've been denied!!!")
            sys.exit()
    elif (game_list == hidden_list):
        wrong_guess_num = 1024
        required_image(wrong_guess_num)
        print("you win! Your word was " + game_word + ".")
        print("Would you like to play again?")
        again = input()
        if again.lower().startswith("y"):
            print("Here we go!")
            hangman_game()
        elif again.lower().startswith("n"):
            print("I've been denied!!!")
            sys.exit()



hangman_game()
