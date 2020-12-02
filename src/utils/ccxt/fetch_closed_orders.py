from logging import getLogger
import traceback
from .get_private_exchange import get_private_exchange

logger = getLogger("__main__").getChild(__name__)


def fetch_closed_orders(exchange_name):
    logger.debug("start")
    logger.debug(exchange_name)
    exchange = get_private_exchange(exchange_name)
    try:
        logger.debug("try")
        closed_orders = exchange.fetch_closed_orders()
        logger.info("success")
    except Exception as error:
        logger.warning("failure")
        logger.warning(error)
        logger.debug(traceback.format_exc())
        closed_orders = None
    logger.debug(closed_orders)
    logger.debug("end")
    return closed_orders
