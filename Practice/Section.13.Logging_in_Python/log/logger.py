import logging
#configuring logging
logging.basicConfig(
    filename='example.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',

    datefmt='%Y-%m-%d %H:%M:%S'
)
