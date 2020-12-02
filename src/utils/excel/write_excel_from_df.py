import traceback
from logging import getLogger

logger = getLogger("__main__").getChild(__name__)


def write_excel_from_df(df, file_path, sheet_name):
    logger.debug("start")
    try:
        logger.debug("try")
        df.to_excel(file_path, sheet_name=sheet_name, index=False)
        logger.info("success")
    except Exception as error:
        logger.error("failure")
        logger.error(error)
        logger.debug(traceback.format_exc())
    logger.debug("end")
