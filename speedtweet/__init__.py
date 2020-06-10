from .utils.version import __version__

import logging

from speedtweet.utils.logger import setup_logging
setup_logging()

from .speedtweet import Speed
