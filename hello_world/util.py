"""
Provides utility functions for hello_world
"""
from hello_world.decorators import *

@uses_e
@uses_h
@uses_l
@uses_o
def get_first_word(letter_e = None, letter_h = None,
                   letter_l = None, letter_o = None):
    return '{0}{1}{2}{2}{3}'.format(letter_h,
                                    letter_e,
                                    letter_l,
                                    letter_o)

@uses_d
@uses_l
@uses_o
@uses_r
@uses_w
def get_second_word(letter_d = None, letter_l = None,
                    letter_o = None, letter_r = None,
                    letter_w = None):
    return '{0}{1}{2}{3}{4}'.format(letter_w,
                                    letter_o,
                                    letter_r,
                                    letter_l,
                                    letter_d)

def get_word(word_number):
    if word_number == 0:
        return get_first_word()
    elif word_number == 1:
        return get_second_word()
    else:
        raise AttributeError("Word index out of range (only 0 and 1 are allowed)")

def display_text(text):
    """
    Displays text on the output
    :param text: the text to displays
    """
    print(text)