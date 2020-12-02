import traceback
from logging import getLogger
from .read_config_as_df import read_config_as_df

logger = getLogger("__main__").getChild(__name__)


def get_api_secret(exchange_name):
    logger.debug("start")
    logger.debug(exchange_name)
    config_api_df = read_config_as_df("api")
    try:
        logger.debug("try search exchange api config")
        config_api_exchange_df = config_api_df[
            config_api_df["exchange_name"] == exchange_name
        ]
        logger.info("success")
    except Exception as error:
        logger.error("failure")
        logger.error(error)
        logger.debug(traceback.format_exc())
        config_api_exchange_df = None
    try:
        logger.debug("try get_api_secret")
        api_secret = config_api_exchange_df.iloc[0]["api_secret"]
        logger.info("success")
    except Exception as error:
        logger.error("failure")
        logger.error(error)
        logger.debug(traceback.format_exc())
        api_secret = ""
    logger.debug("end")
    return api_secret
