import traceback
from logging import getLogger
import pandas as pd
from .read_excel_as_df import read_excel_as_df
from .write_excel_from_df import write_excel_from_df

logger = getLogger("__main__").getChild(__name__)


def add_excel_from_df(add_df, file_path, model):
    logger.debug("start")
    logger.debug(add_df)
    logger.debug(file_path)
    original_df = read_excel_as_df("data.xlsx", model)
    try:
        logger.debug("try search exchange api config")
        result_df = pd.concat([original_df, add_df])
        logger.info("success")
    except Exception as error:
        logger.error("failure")
        logger.error(error)
        logger.debug(traceback.format_exc())
        result_df = None
    logger.debug(result_df)
    try:
        logger.debug("try")
        if result_df is not None:
            write_excel_from_df(result_df, "data.xlsx", model)
    except Exception as error:
        logger.error("failure")
        logger.error(error)
        logger.debug(traceback.format_exc())
    logger.debug("end")
    return result_df
