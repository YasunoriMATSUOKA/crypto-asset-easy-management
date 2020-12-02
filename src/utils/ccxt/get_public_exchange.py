from logging import getLogger
import ccxt

logger = getLogger("__main__").getChild(__name__)


def get_public_exchange(exchange_name):
    logger.debug("start")
    logger.debug(exchange_name)
    exchange = eval("ccxt." + exchange_name + "()")
    logger.debug(exchange)
    logger.debug("end")
    return exchange
