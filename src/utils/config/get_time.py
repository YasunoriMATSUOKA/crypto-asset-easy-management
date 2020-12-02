import traceback
from logging import getLogger
from .read_config_as_df import read_config_as_df

logger = getLogger("__main__").getChild(__name__)


def get_time(period):
    logger.debug("start")
    logger.debug(period)
    config_time_df = read_config_as_df("time")
    logger.debug(config_time_df)
    try:
        logger.debug("try search period config")
        config_time_df = config_time_df[
            config_time_df["period"] == period
        ]
        logger.info("success")
    except Exception as error:
        logger.error("failure")
        logger.error(error)
        logger.debug(traceback.format_exc())
        config_time_df = None
    logger.debug(config_time_df)
    try:
        logger.debug("try")
        trade_time = config_time_df.iloc[0]["time"]
        logger.info("success")
    except Exception as error:
        logger.error("failure")
        logger.error(error)
        logger.debug(traceback.format_exc())
        trade_time = None
    logger.debug(trade_time)
    logger.debug("end")
    return trade_time
