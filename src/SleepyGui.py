from src.Sleeper import sleeper
from src.Kasa import KasaAPI

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,QComboBox, QPushButton, QAction, QLineEdit, QMessageBox, QDesktopWidget
from PyQt5.QtCore import pyqtSlot

class SleepyGui(QMainWindow):

  def __init__(self):
    super().__init__()
    self.title = 'Sleepy Times :)'
    self.left = 10
    self.top = 10
    self.width = 400
    self.height = 250
    self.setup_center()
    self.initUI()
    self.text_input = ''

  def run(self):
    self.initUI()

  def setup_center(self):
    self.qtRectangle = self.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    self.qtRectangle.moveCenter(centerPoint)
    self.move(self.qtRectangle.topLeft())

  def initUI(self):
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)

    # Create textbox
    self.textbox = QLineEdit(self)
    self.textbox.move(20, 20)
    self.textbox.resize(280, 40)

    # Create a button in the window
    self.button = QPushButton('Schedule some sleep!', self)
    self.button.setGeometry(200, 300, 300, 40)
    self.button.move(20, 80)

    self.shutdown_button = QPushButton('Shutdown', self)
    self.shutdown_button.setGeometry(200, 300, 300, 40)
    self.shutdown_button.move(20, 150)

    if KasaAPI.KASA_ENABLED:
      self.cb = QComboBox(self)
      self.cb.addItems(list(KasaAPI.KASA_HOSTS.keys()))
      self.cb.currentIndexChanged.connect(self.selectionchange)
      self.cb.move(300,30)

    # connect button to function on_click
    self.button.clicked.connect(self.schedule_sleep)
    self.shutdown_button.clicked.connect(self.shutdown)
    self.show()
    self.move(self.qtRectangle.topLeft())

  def selectionchange(self, i):

    for count in range(self.cb.count()):
      print(self.cb.itemText(count))
    print("Current index", i, "selection changed ", self.cb.currentText())

  @pyqtSlot()
  def schedule_sleep(self):
    self.text_input = self.textbox.text()
    self.execute_timer()

  @pyqtSlot()
  def shutdown(self):
    if KasaAPI.KASA_ENABLED:
      self.setWindowTitle('Shutting down...')
      KasaAPI.kill_kasa_execute(self.cb.currentText())
      exit(0)

  def execute_timer(self):
    if self.text_input == '':
      self.setWindowTitle('Please provide a number (in minutes)')
      self.textbox.clear()
    elif not str(self.text_input).isnumeric():
      self.setWindowTitle('Please provide a number a valid number (in minutes)')
      self.textbox.clear()
    else:
      self.textbox.clear()
      self.setWindowTitle('Sleeping...')
      sleeper(int(self.text_input), kasaHost=(self.cb.currentText() if KasaAPI.KASA_ENABLED else ''))