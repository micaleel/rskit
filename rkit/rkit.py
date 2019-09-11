__version__ = "0.0.1"

import logging

LOG = logging.getLogger("rkit")


def main():
    LOG.info('Executing rkit version %s', __version__)


def setup_logging(arguments):
    logging.basicConfig(format='%(message)s')
    LOG.setLevel(logging.INFO)
