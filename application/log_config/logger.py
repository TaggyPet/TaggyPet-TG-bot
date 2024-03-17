import logging

info_logger = logging.getLogger(__name__ + ":INFO")
info_logger.setLevel(logging.INFO)

error_logger = logging.getLogger(__name__ + ":ERROR")
error_logger.setLevel(logging.ERROR)

logger_formatter = logging.Formatter(fmt="%(name)s %(asctime)s %(levelname)s %(message)s")
info_logger_handler = logging.FileHandler(filename="logs/tg-core-info.log", mode="w")
error_logger_handler = logging.FileHandler(filename="logs/tg-core-error.log", mode="a")

info_logger_handler.setFormatter(logger_formatter)
error_logger_handler.setFormatter(logger_formatter)

info_logger.addHandler(info_logger_handler)
error_logger.addHandler(error_logger_handler)
