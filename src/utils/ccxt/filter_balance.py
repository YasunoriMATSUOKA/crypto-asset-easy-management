from logging import getLogger
import traceback

logger = getLogger("__main__").getChild(__name__)

# type = "free"
# type = "used"
# type = "total"


def filter_balance(balances, type, ticker):
    logger.debug("start")
    logger.debug(balances)
    logger.debug(type)
    logger.debug(ticker)
    try:
        logger.debug("try")
        balance = balances[type][ticker]
        logger.info("success")
    except Exception as error:
        logger.warning("failure")
        logger.warning(error)
        logger.debug(traceback.format_exc())
        balance = None
    logger.debug(balance)
    logger.debug("end")
    return balance
