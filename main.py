import traceback
from logging import getLogger, handlers, StreamHandler, Formatter, DEBUG, INFO, WARNING, ERROR, CRITICAL, basicConfig
from src.start import start


def main():
    logger.info("start")
    start()


if __name__ == "__main__":
    streamHandler = StreamHandler()
    streamHandler.setLevel(INFO)

    fileHandler = handlers.TimedRotatingFileHandler(
        filename="log/log.log",
        when="MIDNIGHT",
        backupCount=31,
        encoding="utf-8"
    )
    fileHandler.setLevel(DEBUG)

    formatter = "%(asctime)s : %(levelname)s : %(module)s : %(message)s"
    fileHandler.setFormatter(Formatter(formatter))
    streamHandler.setFormatter(Formatter(formatter))

    basicConfig(
        handlers=[streamHandler, fileHandler]
    )

    logger = getLogger(__name__)
    logger.setLevel(DEBUG)

    try:
        main()
    except Exception as error:
        logger.critical(error)
        logger.debug(traceback.format_exc())
