import logging
#create a logger for module one
logger_one = logging.getLogger('module_one')
logger_one.setLevel(logging.DEBUG)
#create a logger for module two
logger_two = logging.getLogger('module_two')
logger_two.setLevel(logging.WARNING)

#configure loggin setting
logging.basicConfig(
    level=logging.DEBUG,
    
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.FileHandler('data.log'), logging.StreamHandler()]
)
logger= logging.getLogger('Artimerts')

#for add fucntion
def add (x, y):
    result = x + y
    logger.debug(f"adding {x} and {y}={result}")
    return result

#for sub function   
def sub (x, y):
    result = x - y
    logger.debug(f"sub {x} and {y}={result}")
    return result

#for mul function
def mul (x, y):
    result = x * y
    logger.debug(f"mul {x} and {y}={result}")
    return result

#for div function
def div (x, y):
    try:
        result = x / y
        logger.debug(f"div {x} and {y}={result}")
        return result
    except ZeroDivisionError:
        logger.error("dividing by zero")
        return None
    
add(1, 2)
sub(1, 2)
mul(1, 2)
div(1, 0)