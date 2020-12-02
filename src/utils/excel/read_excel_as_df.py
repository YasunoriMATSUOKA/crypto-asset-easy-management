from logging import getLogger
import pandas as pd
import traceback

logger = getLogger("__main__").getChild(__name__)


def read_excel_as_df(file_path, sheet_name):
    logger.debug("start")
    logger.debug(file_path)
    logger.debug(sheet_name)
    try:
        logger.debug("try")
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        logger.info("success")
    except Exception as error:
        logger.error("failure")
        logger.error(error)
        logger.debug(traceback.format_exc())
        df = None
    logger.debug("end")
    return df
