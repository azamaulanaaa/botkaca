# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# makes module load by import *

from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]