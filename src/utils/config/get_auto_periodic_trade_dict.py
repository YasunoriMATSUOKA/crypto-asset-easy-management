import traceback
from logging import getLogger
from .read_config_as_df import read_config_as_df

logger = getLogger("__main__").getChild(__name__)


def get_auto_periodic_trade_dict():
    logger.debug("start")
    config_auto_periodic_trade_df = read_config_as_df("auto_periodic_trade")
    try:
        logger.debug("try convert df to dict")
        auto_periodic_trade_dict = config_auto_periodic_trade_df.to_dict(
            orient="records"
        )
        logger.info("success")
    except Exception as error:
        logger.error("failure")
        logger.error(error)
        logger.debug(traceback.format_exc())
        auto_periodic_trade_dict = None
    logger.debug(auto_periodic_trade_dict)
    logger.debug("end")
    return auto_periodic_trade_dict
