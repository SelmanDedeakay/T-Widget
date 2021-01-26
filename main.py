from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import *
from MainWindow_python import *
import sys


class TranslateApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


uygulama = QApplication([])
pencere = TranslateApp()
pencere.show()
uygulama.exec_()
