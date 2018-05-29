#!/usr/bin/env python3
#-*-coding:utf-8-*-
#TODO
#highlight, see: https://wiki.python.org/moin/PyQt/Python%20syntax%20highlighting
# http://carsonfarmer.com/2009/07/syntax-highlighting-with-pyqt/
import sys

from UI.main import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
from PyQt5.QtWebKit import *

import re
import signal

from MainWindow import *

def sigal_int_handler(*args):
    QApplication.quit()

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	app = QApplication(sys.argv)
	window = MainWindow()

	window.show()
	
	sys.exit(app.exec_())
