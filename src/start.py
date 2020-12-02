import time
import traceback
from logging import getLogger
import schedule
from src.utils.config.get_auto_periodic_trade_dict import get_auto_periodic_trade_dict
from .set_schedule import set_schedule

logger = getLogger("__main__").getChild(__name__)


def start():
    logger.debug("start")
    auto_periodic_trade_dict = get_auto_periodic_trade_dict()
    for trade_config in auto_periodic_trade_dict:
        try:
            logger.debug("try get auto periodic trade config")
            exchange_name = trade_config["exchange_name"]
            logger.debug(exchange_name)
            pair = trade_config["pair"]
            logger.debug(pair)
            type = trade_config["type"]
            logger.debug(type)
            side = trade_config["side"]
            logger.debug(side)
            amount = trade_config["amount"]
            logger.debug(amount)
            unit = trade_config["unit"]
            logger.debug(unit)
            period = trade_config["period"]
            logger.debug(period)
            try:
                logger.debug("try set schedule")
                set_schedule(
                    period,
                    exchange_name,
                    pair,
                    type,
                    side,
                    amount,
                    unit,
                    schedule
                )
                logger.info("success")
            except Exception as error:
                logger.error("failure")
                logger.error(error)
                logger.debug(traceback.format_exc())
        except Exception as error:
            logger.error("failure")
            logger.error(error)
            logger.debug(traceback.format_exc())
    while True:
        schedule.run_pending()
        time.sleep(1)
