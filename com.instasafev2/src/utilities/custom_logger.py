import inspect
import logging

def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", mode='a')# mode  a means append it override old logs and automation.log is log file
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(lineno)d - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
