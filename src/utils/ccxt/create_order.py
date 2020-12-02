from logging import getLogger
import traceback
import datetime
import pandas as pd

from src.utils.excel.add_excel_from_df import add_excel_from_df
from .get_private_exchange import get_private_exchange

logger = getLogger("__main__").getChild(__name__)

# type = "limit"
# type = "market"
# side = "buy"
# side = "sell"
# amount, price is number
# if type is "market", price is not necessary


def create_order(exchange_name, pair, type, side, amount, price=None):
    logger.debug("start")
    start_at = datetime.datetime.now()
    logger.debug(exchange_name)
    logger.debug(pair)
    logger.debug(type)
    logger.debug(side)
    logger.debug(amount)
    logger.debug(price)
    exchange = get_private_exchange(exchange_name)
    is_success = False
    try:
        logger.debug("try")
        if type == "limit":
            result = exchange.create_order(
                pair,
                type=type,
                side=side,
                amount=str(amount),
                price=str(price)
            )
            is_success = True
        elif type == "market":
            result = exchange.create_order(
                pair,
                type=type,
                side=side,
                amount=str(amount)
            )
            is_success = True
        else:
            result = None
            logger.error("failure")
            return result
    except Exception as error:
        logger.warning("failure")
        logger.warning(error)
        logger.debug(traceback.format_exc())
        result = None
    if result is not None:
        logger.info("success")
        logger.debug(result)
    else:
        logger.warning("retry")
        try:
            logger.debug("try")
            if type == "limit":
                result = exchange.create_order(
                    pair,
                    type=type,
                    side=side,
                    amount=str(amount),
                    price=str(price)
                )
                is_success = True
                logger.info("success")
            elif type == "market":
                result = exchange.create_order(
                    pair,
                    type=type,
                    side=side,
                    amount=str(amount)
                )
                is_success = True
                logger.info("success")
            else:
                result = None
            if result is None:
                logger.error("failure")
        except Exception as error:
            logger.error("failure")
            logger.error(error)
            logger.debug(traceback.format_exc())
            result = None
        else:
            logger.error("failure")
    end_at = datetime.datetime.now()
    logger.debug(is_success)
    try:
        if is_success:
            df_order_info = pd.DataFrame(
                [[exchange_name, pair, type, side, amount, price, start_at, end_at]],
                columns=["exchange_name", "pair", "type",
                         "side", "amount", "price", "start_at", "end_at"],
                index=[0]
            )
            add_excel_from_df(df_order_info, "data.xlsx", "trade_record")
    except Exception as error:
        logger.warning("failure")
        logger.warning(error)
        logger.debug(traceback.format_exc())
    logger.debug(result)
    logger.debug("end")
    return result
