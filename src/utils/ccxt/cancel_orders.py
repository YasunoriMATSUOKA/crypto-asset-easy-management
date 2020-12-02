from logging import getLogger
import traceback
from .cancel_order import cancel_order

logger = getLogger("__main__").getChild(__name__)


def cancel_orders(exchange_name, orders):
    logger.debug("start")
    logger.debug(exchange_name)
    logger.debug(orders)
    results = []
    for order in orders:
        logger.debug(order)
        try:
            logger.debug("try search order_id")
            order_id = order["id"]
            logger.info("success")
        except Exception as error:
            logger.warning("failure")
            logger.warning(error)
            logger.debug(traceback.format_exc())
            order_id = None
        logger.debug(order_id)
        if order_id is not None:
            result = cancel_order(exchange_name, order_id)
        else:
            result = None
        results.append(result)
    logger.debug(results)
    logger.debug("end")
    return results
