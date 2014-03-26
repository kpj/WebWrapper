import sys
from PyQt5 import QtWidgets

import python.gui, python.js_interface


def main():
	app = QtWidgets.QApplication(sys.argv)

	# create main window
	view = python.gui.Viewer()
	main_window = python.gui.MainWindow(view)

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
