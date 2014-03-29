import sys
from PyQt5 import QtWidgets

import python.gui, python.js_interface


def main():
	app = QtWidgets.QApplication(sys.argv)

	# create main window
	view = python.gui.Viewer()
	window = python.gui.MainWindow(view)

	# create js interface
	jsi = python.js_interface.JavascriptInterface(window, view)
	view.set_js_interface(jsi)

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
