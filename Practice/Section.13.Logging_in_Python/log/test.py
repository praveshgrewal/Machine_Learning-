from logger import logging

def add(x, y):

    logging.debug('Adding %s and %s', x, y)
    return x + y

logging.debug("the addition functin is called")

add(1, 2)

def sub(x, y):

    logging.debug('sub %s and %s', x, y)
    return x + y

logging.debug("the substraction functin is called")

add(1, 2)

