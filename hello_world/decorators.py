"""
decorators for use with hello_world to keep the code cleaner
"""
from functools import wraps

def uses_d(f):
    @wraps(f)
    def with_d(*args, **kwargs):
        return f(*args, letter_d = 'd', **kwargs)

    return with_d

def uses_e(f):
    @wraps(f)
    def with_e(*args, **kwargs):
        return f(*args, letter_e = 'e', **kwargs)

    return with_e

def uses_h(f):
    @wraps(f)
    def with_h(*args, **kwargs):
        return f(*args, letter_h = 'h', **kwargs)

    return with_h

def uses_l(f):
    @wraps(f)
    def with_l(*args, **kwargs):
        return f(*args, letter_l = 'l', **kwargs)

    return with_l

def uses_o(f):
    @wraps(f)
    def with_o(*args, **kwargs):
        return f(*args, letter_o = 'o', **kwargs)

    return with_o

def uses_r(f):
    @wraps(f)
    def with_r(*args, **kwargs):
        return f(*args, letter_r = 'r', **kwargs)

    return with_r

def uses_w(f):
    @wraps(f)
    def with_w(*args, **kwargs):
        return f(*args, letter_w = 'w', **kwargs)

    return with_w



