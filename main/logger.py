import logging
import sys

from dir import local_dir, TEST_MODE

# Clean timber.log up
timber_path = local_dir + '/timber.log'
f = open(timber_path, 'w', encoding='utf-8')
f.close()

file_handler = logging.FileHandler(filename=timber_path, mode='w')
file_handler.setLevel(logging.DEBUG)
file_fmt = logging.Formatter(fmt="%(asctime)s [%(levelname)s] %(filename)s(%(lineno)s) - %(message)s",
                             datefmt="%Y/%m/%d %H:%M:%S")
file_handler.setFormatter(file_fmt)

cmd_handler = logging.StreamHandler()
cmd_handler.setLevel(logging.WARNING)
cmd_fmt = logging.Formatter(fmt="[%(levelname)s] %(message)s")
cmd_handler.setFormatter(cmd_fmt)

timber = logging.getLogger('timber')
timber.setLevel(logging.DEBUG)
timber.addHandler(file_handler)
timber.addHandler(cmd_handler)

if TEST_MODE:
    timber.info('TEST_MODE on')