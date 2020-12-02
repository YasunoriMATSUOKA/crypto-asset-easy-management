from logging import getLogger
import traceback

logger = getLogger("__main__").getChild(__name__)

# type = "free"
# type = "used"
# type = "total"


def filter_balances(balances, type):
    logger.debug("start")
    logger.debug(balances)
    logger.debug(type)
    try:
        logger.debug("try")
        balances = balances[type]
        logger.info("success")
    except Exception as error:
        logger.warning("failure")
        logger.warning(error)
        logger.debug(traceback.format_exc())
        balances = None
    logger.debug(balances)
    logger.debug("end")
    return balances
