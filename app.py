from src.SleepyGui import SleepyGui

import sys
from PyQt5.QtWidgets import  QApplication

# Run the App
if __name__ == "__main__":
    runApp = QApplication(sys.argv)
    gui=SleepyGui()
    runApp.exec_()
