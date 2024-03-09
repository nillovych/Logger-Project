from logger import Logger
from setup_options import CfgFileOption

option = CfgFileOption()

logger = Logger(option)

elements = [1,2]

a = [element for element in elements if element >= 5]

for element in a:
    logger.log(str(element))


