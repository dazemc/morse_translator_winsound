import os
import time

if os.name == 'nt':
    import winsound as ws

BEEP_FREQUENCY = 6000
DOT_DURATION = 400
DASH_DURATION = 1200
LETTER_PAUSE = 1
AFTER_LETTER_PAUSE = 3
WORD_PAUSE = 7
UNIX_DOT = 'speaker-test -t sine -f 1000 -l 1 & sleep .2 && kill -9 $!'
UNIX_DASH = 'speaker-test -t sine -f 1000 -l 1 & sleep .6 && kill -9 $!'


# This is the corresponding value for each letter into morse code.
# (Dots will be *)(Dashes will be -)
morse_letters = {
    'a': ['*', '-'],
    'b': ['-', '*', '*', '*'],
    'c': ['-', '*', '-', '*'],
    'd': ['-', '*', '*'],
    'e': ['*'],
    'f': ['*', '*', '-', '*'],
    'g': ['-', '-', '*'],
    'h': ['*', '*', '*', '*'],
    'i': ['*', '*'],
    'j': ['*', '-', '-', '-'],
    'k': ['-', '*', '-'],
    'l': ['*', '-', '*', '*'],
    'm': ['-', '-'],
    'n': ['-', '*'],
    'o': ['-', '-', '-'],
    'p': ['*', '-', '-', '*'],
    'q': ['-', '-', '*', '-'],
    'r': ['*', '-', '*'],
    's': ['*', '*', '*'],
    't': ['-'],
    'u': ['*', '*', '-'],
    'v': ['*', '*', '*', '-'],
    'w': ['*', '-', '-'],
    'x': ['-', '*', '*', '-'],
    'y': ['-', '*', '-', '-'],
    'z': ['-', '-', '*', '*'],
    '1': ['*', '-', '-', '-', '-'],
    '2': ['*', '*', '-', '-', '-'],
    '3': ['*', '*', '*', '-', '-'],
    '4': ['*', '*', '*', '*', '-'],
    '5': ['*', '*', '*', '*', '*'],
    '6': ['-', '*', '*', '*', '*'],
    '7': ['-', '-', '*', '*', '*'],
    '8': ['-', '-', '-', '*', '*'],
    '9': ['-', '-', '-', '-', '*'],
    '0': ['-', '-', '-', '-', '-'],
}


# pauses between a letter
def letter_pause():
    time.sleep(LETTER_PAUSE)

# pauses after a letter
def after_pause():
    time.sleep(AFTER_LETTER_PAUSE)

# pauses after a word
def word_pause():
    time.sleep(WORD_PAUSE)


def dot():
    ws.Beep(BEEP_FREQUENCY, DOT_DURATION)


def dash():
    ws.Beep(BEEP_FREQUENCY, DASH_DURATION)

# Uses two loops to iterate through the inputted letters and the corresponding codes.
def convert_letters(word):
    converted_string = []
    for v in word:
        for j in morse_letters:
            if v == j:
                converted_string.append(morse_letters[j])
    converted_string.append([' '])  # this is used to separate words
    return converted_string


user_input = input("Enter text to convert to morse: ")
# separate words by spaces and lowercase them
user_input = user_input.lower().split(' ')
for _ in user_input:
    for letters in convert_letters(_):
        for code in letters:
            if code == '*':
                if os.name != 'posix':
                    dot()
                else:
                    os.system(UNIX_DOT)
                letter_pause()
            if code == '-':
                if os.name != 'posix':
                    dash()
                else:
                    os.system(UNIX_DASH)
                letter_pause()
            if code == ' ':
                word_pause()
        after_pause()

