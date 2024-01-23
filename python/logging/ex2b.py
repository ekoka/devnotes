import logging

logger = logging.getLogger('ex2.b')
a_logger = logging.getLogger('ex2.b.a')
b_logger = logging.getLogger('ex2.b.b')
c_logger = logging.getLogger('ex2.b.c')

a_logger.info("info message for A logger")
