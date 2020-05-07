import os
import logging

STREAM_HANDLER = logging.StreamHandler()
STREAM_HANDLER.setFormatter(
    logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(pathname)s:%(lineno)s] %(message)s",
        datefmt="%Y-%m-%d%T%H:%M:%S",
    )
)


class Logger:
    def __init__(self, module: str):
        self.logger = logging.getLogger(module)
        self.logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))
        self.logger.addHandler(STREAM_HANDLER)

    def getLogger(self):
        return self.logger
