from src.Sleeper import sleeper

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot

class SleepyGui(QMainWindow):

  def __init__(self):
    super().__init__()
    self.title = 'Sleepy Times :)'
    self.left = 10
    self.top = 10
    self.width = 400
    self.height = 140
    self.initUI()
    self.text_input = ''

  def run(self):
    self.initUI()

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

    # connect button to function on_click
    self.button.clicked.connect(self.on_click)
    self.show()

  @pyqtSlot()
  def on_click(self):
    self.text_input = self.textbox.text()
    self.execute_timer()
    #QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
    #self.textbox.setText("")

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
      sleeper(int(self.text_input))