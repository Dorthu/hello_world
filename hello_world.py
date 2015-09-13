"""
hello_world - a program to print the phrase 'hello world'
"""
def get_word(word_number):
    if word_number == 0:
        return 'hello'
    elif word_number == 1:
        return 'world'
    else:
        raise AttributeError("Word index out of range (only 0 and 1 are allowed)")

def display_text(text):
    print(text)

MESSAGE = "{} {}".format(get_word(0), get_word(1))

display_text(MESSAGE)