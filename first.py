import math


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Invalid"


def m_sin(x):
    return math.sin(x)


def m_cos(x):
    return math.cos(x)
