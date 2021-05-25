import logging
import sys
import os.path as osp

logging.basicConfig(level=logging.INFO,
                    filename=osp.join(osp.dirname(osp.abspath(__file__)), 'logs/logs.log'),
                    datefmt='%Y/%m/%d %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))

if __name__ == '__main__':
    print(sys.path)
