from logging import getLogger
import traceback
from .get_public_exchange import get_public_exchange

logger = getLogger("__main__").getChild(__name__)


def fetch_order_book(exchange_name, pair):
    logger.debug("start")
    logger.debug(exchange_name)
    logger.debug(pair)
    exchange = get_public_exchange(exchange_name)
    try:
        logger.debug("try")
        order_book = exchange.fetch_order_book(pair)
        logger.info("success")
    except Exception as error:
        logger.warning("failure")
        logger.warning(error)
        logger.debug(traceback.format_exc())
        order_book = None
    logger.debug(order_book)
    logger.debug("end")
    return order_book
