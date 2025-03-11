import logging


logger = logging.getLogger(name='api_Test')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(funcName)s] %(message)s')
fl = logging.FileHandler(filename=r'logs\log.txt', mode='a', encoding='utf8')

fl.setFormatter(formatter)

sl = logging.StreamHandler()
sl.setFormatter(formatter)

logger.addHandler(fl)
logger.addHandler(sl)

fl.close()