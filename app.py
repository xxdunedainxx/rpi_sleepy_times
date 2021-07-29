from src.SleepyGui import SleepyGui

import sys
from PyQt5.QtWidgets import  QApplication
from src.Util import macosx_fix

# Run the App
if __name__ == "__main__":
    macosx_fix()
    runApp = QApplication(sys.argv)
    gui=SleepyGui()
    runApp.exec_()
