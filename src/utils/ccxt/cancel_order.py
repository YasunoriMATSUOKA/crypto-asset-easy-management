import traceback
from logging import getLogger
from .get_private_exchange import get_private_exchange

logger = getLogger("__main__").getChild(__name__)


def cancel_order(exchange_name, order_id):
    logger.debug("start")
    logger.debug(exchange_name)
    logger.debug(order_id)
    exchange = get_private_exchange(exchange_name)
    try:
        logger.debug("try")
        result = exchange.cancel_order(order_id)
        logger.info("success")
    except Exception as error:
        logger.warning("failure")
        logger.warning(error)
        logger.debug(traceback.format_exc())
        result = None
    logger.debug(result)
    logger.debug("end")
    return result
