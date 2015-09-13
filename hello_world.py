"""
hello_world - a program to print the phrase 'hello world'
"""
from hello_world import display_text, get_word

MESSAGE = "{} {}".format(get_word(0), get_word(1))

display_text(MESSAGE)