# GOAL:
# getting track for logging

import logging

LOGGER = logging.getLogger(__name__)

# GOAL:
# create zipfile handler class

from zipfile import ZipFile 
import os 

def func(files_path, outpath): 
    LOGGER.info('Zipping : ' + outpath)
    with ZipFile(outpath,'w') as zip:
        for file in files_path: 
            zip.write(file) 
            os.remove(file)
    LOGGER.info('Zipped : ' + outpath)
    return outpath