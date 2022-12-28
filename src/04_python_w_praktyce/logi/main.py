import logging
import logging.handlers as handlers
import time

logger = logging.getLogger("my_app")
logger.setLevel(logging.INFO)

## Here we define our formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logHandler = handlers.TimedRotatingFileHandler(
    "timed_app.log", when="M", interval=1, backupCount=2
)
logHandler.setLevel(logging.INFO)
## Here we set our logHandler's formatter
logHandler.setFormatter(formatter)

logger.addHandler(logHandler)


def main():
    while True:
        time.sleep(1)
        logger.info("A Sample Log Statement")


main()
