import sys
from PyQt4 import QtGui, QtCore

import python.gui, python.js_interface


def main():
	app = QtGui.QApplication(sys.argv)

	# create main window
	view = python.gui.Viewer()

	#view.page().mainFrame().addToJavaScriptWindowObject(
	#	"PyInterface",
	#	python.js_interface.JavascriptInterface(view)
	#)
	# does not work -> PyInterface = null (in js)

	# only the following approach works
	jsi = python.js_interface.JavascriptInterface(view)
	view.page().mainFrame().addToJavaScriptWindowObject(
		"PyInterface",
		jsi
	)

	main_window = python.gui.MainWindow(view)

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()