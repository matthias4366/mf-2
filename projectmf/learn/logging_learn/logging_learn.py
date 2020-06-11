import logging

logging.basicConfig(
    filename='measuredfood.log',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s\n'
           'File: %(filename)s \n'
           'Line: %(lineno)d \n'
           'Message: %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.warning('This will get logged to a file')
