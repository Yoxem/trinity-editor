from PyQt5.QtCore import *

def label_set_text(self):
	"""set the label text in the interface"""
	_translate = QCoreApplication.translate
	self.label_html.setText(_translate("MainWindow", "HTML"))
	self.label_css.setText(_translate("MainWindow", "CSS"))
	self.label_js.setText(_translate("MainWindow", "JavaScript"))
