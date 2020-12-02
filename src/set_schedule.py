import traceback
import datetime
from logging import getLogger
from src.utils.config.get_time import get_time
from src.utils.config.get_day_of_every_weeks import get_day_of_every_weeks
from src.utils.config.get_day_of_every_months import get_day_of_every_months
from src.execute_order import execute_order

logger = getLogger("__main__").getChild(__name__)


def set_schedule(period, exchange_name, pair, type, side, amount, unit, schedule):
    logger.debug("start")
    logger.debug(period)
    logger.debug(exchange_name)
    logger.debug(pair)
    logger.debug(type)
    logger.debug(side)
    logger.debug(amount)
    logger.debug(unit)
    trade_time = get_time(period)
    if period == "daily":
        try:
            logger.debug("try")
            schedule.every().day.at(trade_time).do(
                execute_order, exchange_name, pair, type, side, amount, unit
            )
            logger.info("success")
        except Exception as error:
            logger.error("failure")
            logger.error(error)
            logger.debug(traceback.format_exc())
    elif period == "weekly":
        day_of_every_weeks = get_day_of_every_weeks(period)
        try:
            logger.debug("try")
            function_string = "schedule.every()." + day_of_every_weeks.lower() + \
                ".at(trade_time).do(execute_order, exchange_name, pair, type, side, amount, unit)"
            logger.debug(function_string)
            eval(function_string)
            logger.info("success")
        except Exception as error:
            logger.error("failure")
            logger.error(error)
            logger.debug(traceback.format_exc())
    elif period == "monthly":
        day_of_every_months = get_day_of_every_months(period)
        try:
            if datetime.datetime.now().day == day_of_every_months:
                schedule.every().day.at(trade_time).do(
                    execute_order, exchange_name, pair, type, side, amount, unit
                )
        except Exception as error:
            logger.error("failure")
            logger.error(error)
            logger.debug(traceback.format_exc())
