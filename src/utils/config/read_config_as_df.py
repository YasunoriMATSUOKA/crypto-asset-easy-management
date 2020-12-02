from logging import getLogger
from ..excel.read_excel_as_df import read_excel_as_df

logger = getLogger("__main__").getChild(__name__)


def read_config_as_df(model):
    logger.debug("start")
    config_df = read_excel_as_df("config.xlsx", model)
    logger.debug("end")
    return config_df
