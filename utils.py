import random as r
import functools

from time import sleep


def generate_valid_email():
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    extra_symbols = '+-_'
    s = ''

    for i in range(4):
        s += r.choice(symbols) + r.choice(numbers)
    
    s += r.choice(extra_symbols)

    return s + '@tst.whotrades.org'

def generate_invalid_email():
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    extra_symbols = r'`~!@#$%^&*()=№,<>?:;"}{[]\\' + "'"
    s = ''

    for i in range(6):
        s += r.choice(symbols) + r.choice(extra_symbols)

    return s + '@tst.whotrades.org'


def wait(delay=3):
        def deco(func):
            @functools.wraps(func)
            def inner(*args, **kwargs):
                sleep(delay)
                return func(*args, **kwargs)
            return inner
        return deco
