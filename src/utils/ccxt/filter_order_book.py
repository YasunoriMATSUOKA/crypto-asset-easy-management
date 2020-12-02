from logging import getLogger
import traceback

logger = getLogger("__main__").getChild(__name__)

# type = "asks"
# type = "bids"


def filter_order_book(order_book, type):
    logger.debug("start")
    logger.debug(order_book)
    logger.debug(type)
    try:
        logger.debug("try")
        typed_order_book = order_book[type]
        logger.info("success")
    except Exception as error:
        logger.warning("failure")
        logger.warning(error)
        logger.debug(traceback.format_exc())
        typed_order_book = None
    logger.debug(typed_order_book)
    logger.debug("end")
    return typed_order_book
