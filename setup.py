# pip install setuptools
# pip install ./

import sys


if (sys.version_info.major < 3):
    print('PYTHON VERSION MUST BE 3 OR GREATER!!')
    exit(1)

from src.Util import installer

installer()