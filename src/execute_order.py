import traceback
from logging import getLogger
from decimal import Decimal, ROUND_HALF_UP
from src.utils.config.get_min_order_unit import get_min_order_unit
from src.utils.config.get_min_order_amount import get_min_order_amount
from src.utils.config.get_min_price_unit import get_min_price_unit
from src.utils.ccxt.fetch_order_book import fetch_order_book
from src.utils.ccxt.filter_order_book import filter_order_book
from src.utils.ccxt.create_order import create_order
from src.utils.ccxt.create_order import create_order

logger = getLogger("__main__").getChild(__name__)


def execute_order(exchange_name, pair, type, side, amount, unit):
    logger.debug("start")
    logger.debug(exchange_name)
    logger.debug(pair)
    logger.debug(type)
    logger.debug(side)
    logger.debug(amount)
    logger.debug(unit)
    min_order_amount = get_min_order_amount(exchange_name, pair)
    min_order_unit = get_min_order_unit(exchange_name, pair)
    min_price_unit = get_min_price_unit(exchange_name, pair)
    order_book = fetch_order_book(exchange_name, pair)
    asks = filter_order_book(order_book, "asks")
    bids = filter_order_book(order_book, "bids")
    try:
        logger.debug("try price calculate")
        if side == "buy":
            if min_price_unit < 1:
                price = float(Decimal(str(asks[0][0] - min_price_unit)).quantize(
                    Decimal(str(min_price_unit)), rounding=ROUND_HALF_UP))
            else:
                price = int(asks[0][0] - min_price_unit)
            logger.info("success")
        elif side == "sell":
            if min_price_unit < 1:
                price = float(Decimal(str(bids[0][0] + min_price_unit)).quantize(
                    Decimal(str(min_price_unit)), rounding=ROUND_HALF_UP))
            else:
                price = int(bids[0][0] + min_price_unit)
            logger.info("success")
        else:
            logger.error("failure")
            logger.error("side:" + side + " is not supported")
            price = None
    except Exception as error:
        logger.error("failure")
        logger.error(error)
        logger.debug(traceback.format_exc())
        price = None
    logger.debug(price)
    try:
        logger.debug("try amount calculate")
        if unit == "JPY":
            amount = amount / price
            if min_order_unit < 1:
                amount = float(Decimal(str(amount)).quantize(
                    Decimal(str(min_order_unit)), rounding=ROUND_HALF_UP))
            else:
                amount = int(amount)
            logger.info("success")
        elif unit == pair.split("/")[0]:
            if min_order_unit < 1:
                amount = float(Decimal(str(amount)).quantize(
                    Decimal(str(min_order_unit)), rounding=ROUND_HALF_UP))
            else:
                amount = int(amount)
            logger.info("success")
        else:
            logger.error("failure")
            logger.error("pair:" + pair + " and unit:" + unit + " mismatch")
            amount = None
    except Exception as error:
        logger.error("failure")
        logger.error(error)
        logger.debug(traceback.format_exc())
        amount = None
    logger.debug(amount)
    if (price is not None) and (amount is not None):
        if amount >= min_order_amount:
            result = create_order(
                exchange_name,
                pair,
                type,
                side,
                amount,
                price
            )
        else:
            logger.error("order amount is to small")
            result = None
    else:
        logger.error("bad price or bad amount")
        result = None
    logger.debug("end")
    return result
