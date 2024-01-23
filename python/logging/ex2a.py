import logging

logger = logging.getLogger('ex2')
logger.setLevel(logging.INFO)

fh = logging.FileHandler("outputs/ex2.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - "
                              "%(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.info("info message")
logger.info("filemode: %s" % fh.mode)
logger.error("error message")
