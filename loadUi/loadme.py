from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QPushButton
from PyQt5 import uic
import sys
import os
class UI(QMainWindow):
  def __init__(self):
    super(UI, self).__init__()
    uic.loadUi("loadUi/loadme.ui", self)
    self.pushButton.clicked.connect(self.clicker)
    self.show()

  def clicker(self):
    text = self.lineEdit.text()
    self.label.setText(f"You typed {text}")
    self.lineEdit.clear()
# initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()