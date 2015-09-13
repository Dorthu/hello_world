"""
Provides utility functions for hello_world
"""
from hello_world.words import uses_space, without_trailing_space
from hello_world.words import words

@uses_space
@without_trailing_space
def get_message(space_character=None):
    message = ""
    for word in words():
        message += word + space_character

    return message

def display_text(text):
    """
    Displays text on the output
    :param text: the text to displays
    """
    print(text)