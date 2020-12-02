from logging import getLogger
import traceback
from .get_private_exchange import get_private_exchange

logger = getLogger("__main__").getChild(__name__)


def fetch_balances(exchange_name):
    logger.debug("start")
    logger.debug(exchange_name)
    exchange = get_private_exchange(exchange_name)
    try:
        logger.debug("try")
        balances = exchange.fetch_balance()
        logger.info("success")
    except Exception as error:
        logger.warning("failure")
        logger.warning(error)
        logger.debug(traceback.format_exc())
        balances = None
    logger.debug(balances)
    logger.debug("end")
    return balances
