import traceback
from logging import getLogger
from .read_config_as_df import read_config_as_df

logger = getLogger("__main__").getChild(__name__)


def get_min_price_unit(exchange_name, pair):
    logger.info("start")
    logger.debug(exchange_name)
    logger.debug(pair)
    config_ticker_df = read_config_as_df("ticker")
    try:
        logger.debug("try search ticker exchange pair config")
        config_ticker_exchange_df = config_ticker_df[
            config_ticker_df["exchange_name"] == exchange_name
        ]
        config_ticker_exchange_pair_df = config_ticker_exchange_df[
            config_ticker_exchange_df["pair"] == pair
        ]
        logger.info("success")
    except Exception as error:
        logger.error("failure")
        logger.error(error)
        logger.debug(traceback.format_exc())
        config_ticker_exchange_pair_df = None
    try:
        logger.debug("try")
        min_price_unit = config_ticker_exchange_pair_df.iloc[0]["min_price_unit"]
        logger.info("success")
    except Exception as error:
        logger.error("failure")
        logger.error(error)
        logger.debug(traceback.format_exc())
        min_price_unit = None
    logger.debug(min_price_unit)
    logger.debug("end")
    return min_price_unit
