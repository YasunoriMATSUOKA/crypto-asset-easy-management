from logging import getLogger
import ccxt
from ..config.get_api_key import get_api_key
from ..config.get_api_secret import get_api_secret

logger = getLogger("__main__").getChild(__name__)


def get_private_exchange(exchange_name):
    logger.debug("start")
    logger.debug(exchange_name)
    exchange = eval("ccxt." + exchange_name +
                    "({'apiKey': '" + get_api_key(exchange_name) + "', '" + "secret': '" + get_api_secret(exchange_name) + "'})")
    logger.debug("end")
    return exchange
