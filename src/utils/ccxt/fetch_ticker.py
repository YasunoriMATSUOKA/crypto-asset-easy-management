from logging import getLogger
import traceback
from .get_public_exchange import get_public_exchange

logger = getLogger("__main__").getChild(__name__)


def fetch_ticker(exchange_name, pair):
    logger.debug("start")
    logger.debug(exchange_name)
    logger.debug(pair)
    exchange = get_public_exchange(exchange_name)
    try:
        logger.debug("try")
        ticker_info = exchange.fetch_ticker(pair)
        logger.info("success")
    except Exception as error:
        logger.warning("failure")
        logger.warning(error)
        logger.debug(traceback.format_exc())
        ticker_info = None
    logger.debug(ticker_info)
    logger.debug("end")
    return ticker_info
