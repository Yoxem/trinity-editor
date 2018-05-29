#!/usr/bin/env python3
#-*-coding:utf-8-*-
from .ui_add_splitter_and_textedit import ui_add_splitter_and_textedit
from .label_set_text import label_set_text
from .change_html import change_html
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow
from UI.main import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.ui_add_splitter_and_textedit()
		self.label_set_text()


		self.html_textedit.textChanged.connect(self.change_html)
		self.css_textedit.textChanged.connect(self.change_html)
		self.js_textedit.textChanged.connect(self.change_html)


	def change_html(self):
		change_html(self)

	def ui_add_splitter_and_textedit(self):
		ui_add_splitter_and_textedit(self)

	def label_set_text(self):
		label_set_text(self)
