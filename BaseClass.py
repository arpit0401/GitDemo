import inspect
import logging
class Baseclass:
      def test_loggingDemo(self):
            loggerName = inspect.stack()[1][3]
            logger = logging.getLogger(loggerName)
            filehander = logging.FileHandler("logfile.log")
            format = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s ")

            filehander.setFormatter(format)

            logger.addHandler(filehander)

            logger.setLevel(logging.DEBUG)
            return logger
