"""
Generates data for use in hello_world
"""
from .words import get_word

def words():
    """
    A generator used to get the words for the message
    :return: words in the message, one at a time
    """
    for word in (0, 1):
        yield get_word(word)

