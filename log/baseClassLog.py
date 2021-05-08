import inspect
import logging


# integrating pytest logs into test cases and html reports
# instead of printing msg in console,we have using logs for msgs and integrate with html reports

class BaseClass:

    def getlogger(self):

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler('logfile.log')
        formater = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
        filehandler.setFormatter(formater)

        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)

        return logger
