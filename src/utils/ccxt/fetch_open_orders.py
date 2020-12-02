from logging import getLogger
import traceback
from .get_private_exchange import get_private_exchange

logger = getLogger("__main__").getChild(__name__)


def fetch_open_orders(exchange_name):
    logger.debug("start")
    logger.debug(exchange_name)
    exchange = get_private_exchange(exchange_name)
    try:
        logger.debug("try")
        open_orders = exchange.fetch_open_orders()
        logger.info("success")
    except Exception as error:
        logger.warning("failure")
        logger.warning(error)
        logger.debug(traceback.format_exc())
        open_orders = None
    logger.debug(open_orders)
    logger.debug("end")
    return open_orders
