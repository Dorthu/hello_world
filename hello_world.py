"""
hello_world - a program to print the phrase 'hello world'
"""

def get_letter(letter_index):
    return "abcdefghijklmnopqrstuvwxyz"[letter_index]

def get_word(word_number):
    if word_number == 0:
        return '{0}{1}{2}{2}{3}'.format(get_letter(7),
                                        get_letter(4),
                                        get_letter(11),
                                        get_letter(14))
    elif word_number == 1:
        return '{0}{1}{2}{3}{4}'.format(get_letter(22),
                                        get_letter(14),
                                        get_letter(17),
                                        get_letter(11),
                                        get_letter(3))
    else:
        raise AttributeError("Word index out of range (only 0 and 1 are allowed)")

def display_text(text):
    print(text)

MESSAGE = "{} {}".format(get_word(0), get_word(1))

display_text(MESSAGE)