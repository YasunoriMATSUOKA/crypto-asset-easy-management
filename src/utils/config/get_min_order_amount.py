import traceback
from logging import getLogger
from .read_config_as_df import read_config_as_df

logger = getLogger("__main__").getChild(__name__)


def get_min_order_amount(exchange_name, pair):
    logger.debug("start")
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
        min_order_amount = config_ticker_exchange_pair_df.iloc[0]["min_order_amount"]
        logger.info("success")
    except Exception as error:
        logger.error("failure")
        logger.error(error)
        logger.debug(traceback.format_exc())
        min_order_amount = None
    logger.debug(min_order_amount)
    logger.debug("end")
    return min_order_amount
