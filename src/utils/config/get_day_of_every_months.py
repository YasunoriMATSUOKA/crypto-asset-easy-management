import traceback
from logging import getLogger
from .read_config_as_df import read_config_as_df

logger = getLogger("__main__").getChild(__name__)


def get_day_of_every_months(period):
    logger.debug("start")
    logger.debug(period)
    config_time_df = read_config_as_df("time")
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
    try:
        logger.debug("try")
        day_of_every_months = config_time_df.iloc[0]["day_of_every_months"]
        logger.info("success")
    except Exception as error:
        logger.error("failure")
        logger.error(error)
        logger.debug(traceback.format_exc())
        day_of_every_months = None
    logger.debug(day_of_every_months)
    logger.debug("end")
    return day_of_every_months
