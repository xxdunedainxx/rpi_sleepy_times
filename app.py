from src.SleepyGui import SleepyGui

import sys
from PyQt5.QtWidgets import  QApplication
from src.Util import macosx_fix
from src.LogFactory import LogFactory
from src.ErrorFactory import errorStackTrace
from src.Sleeper import sleeper

# Run the App
if __name__ == "__main__":
    try:
        LogFactory.main_log()
        LogFactory.MAIN_LOG.info("start sleeper")
        #sleeper()
        runApp = QApplication(sys.argv)
        gui=SleepyGui()
        runApp.exec_()
        exit(0)
    except Exception as e:
        LogFactory.MAIN_LOG.error(f"{errorStackTrace(e)}")
        exit(1)