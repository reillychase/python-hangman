import random

word_list = '''
put
your
hangman
words
here
one
per
line
'''
class game:
    words = []
    for line in word_list.split():
        words.append(line)
    chosen_word = (random.choice(words))
    chosen_word_letters = list(chosen_word)
    chosen_word_num_letters = []
    for letter in chosen_word_letters:
        if letter not in chosen_word_num_letters:
            chosen_word_num_letters.append(letter)
    length_chosen_word = len(chosen_word)
    wrong_guesses = 0
    correct_guesses = []
    guessed_letters = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

def new_game():
    game.words = []
    for line in word_list.split():
        game.words.append(line)
    game.chosen_word = (random.choice(game.words))
    game.chosen_word_letters = list(game.chosen_word)
    game.chosen_word_num_letters = []
    for letter in game.chosen_word_letters:
        if letter not in game.chosen_word_num_letters:
            game.chosen_word_num_letters.append(letter)
    game.length_chosen_word = len(game.chosen_word)
    game.wrong_guesses = 0
    game.correct_guesses = []
    game.guessed_letters = []
    game.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u','v', 'w', 'x', 'y', 'z']

def print_hangman(wrong_guesses):
    if (wrong_guesses == 0):
        print '''
            ______
            |    |
                 |
                 |
                 |
       __________|__________

        '''
    elif (wrong_guesses == 1):
        print '''
            ______
            |    |
            O    |
                 |
                 |
       __________|__________

        '''
    elif (wrong_guesses == 2):
        print '''
            ______
            |    |
            O    |
            |    |
                 |
       __________|__________

        '''
    elif (wrong_guesses == 3):
        print '''
            ______
            |    |
            O    |
            |\   |
                 |
       __________|__________

        '''
    elif (wrong_guesses == 4):
        print '''
            ______
            |    |
            O    |
           /|\   |
                 |
       __________|__________

        '''
    elif (wrong_guesses == 5):
        print '''
            ______
            |    |
            O    |
           /|\   |
             \   |
       __________|__________

        '''
    else:
        print '''
            ______
            |    |
            O    |
           /|\   |
           / \   |
       __________|__________

        '''

def print_word():
    i = 0
    while (i < game.length_chosen_word):
        if game.chosen_word_letters[i] in game.correct_guesses:
            print ' ',
            print game.chosen_word_letters[i],
            print ' ',
        else:
            print '''___''',
        i = i + 1

def print_guessed_letters():
    guessed_letter_len = len(game.guessed_letters) - 1
    print '\n\n'
    for letter in game.guessed_letters:
        if letter != game.guessed_letters[guessed_letter_len]:
            print letter + ',',
        else:
            print letter,
    print '\n'

while True:
    print_guessed_letters()
    print_hangman(game.wrong_guesses)
    print_word()
    while True:
        print "\n\nGuess a letter: ",
        letter = raw_input().lower()
        if letter not in game.alphabet:
            print "\n\nERROR: Only 1 letter, A-Z allowed!"
            continue
        elif letter in game.guessed_letters:
            print "\n\nERROR: You already guessed '" + letter + "'!"
            continue
        break

    game.guessed_letters.append(letter)

    if letter not in game.chosen_word:
        game.wrong_guesses = game.wrong_guesses + 1
    else:
        game.correct_guesses.append(letter)

    if (game.wrong_guesses > 5):
        print_guessed_letters()
        print_hangman(game.wrong_guesses)
        print_word()
        print '\n\nGAME OVER!'
        while True:
            play_again = raw_input('\n\nDo you want to play again? [y/n]: ').lower()
            if play_again != 'y' and play_again != 'n':
                print "\n\nERROR: Please enter 'y' for yes or 'n' for no"
                continue
            else:
                break

        if play_again == 'y':
            new_game()
            continue
        else:
            break

    if len(game.correct_guesses) == len(game.chosen_word_num_letters):
        print_guessed_letters()
        print_hangman(game.wrong_guesses)
        print_word()
        print '\n\nCongratulations, you win!'
        while True:
            play_again = raw_input('\n\nDo you want to play again? [y/n]: ').lower()
            if play_again != 'y' and play_again != 'n':
                print "\n\nERROR: Please enter 'y' for yes or 'n' for no"
                continue
            else:
                break

        if play_again == 'y':
            new_game()
            continue
        else:
            break

raw_input('\n\nPress enter to exit...')


