__version__ = "0.0.1"

import logging

LOG = logging.getLogger("rskit")


def main():
    LOG.info('Executing rskit version %s', __version__)


def setup_logging():
    logging.basicConfig(format='%(message)s')
    LOG.setLevel(logging.INFO)
