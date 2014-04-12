import sys
from PyQtX import QtWidgets

import python.gui, python.js_interface, python.arg_parser


def main():
	# handle cmd-line arguments
	args = python.arg_parser.get_args()

	# create main window
	app = QtWidgets.QApplication(sys.argv)

	view = python.gui.Viewer(args)
	window = python.gui.MainWindow(view)

	# create js interface
	jsi = python.js_interface.JavascriptInterface(window, view, args)
	view.set_js_interface(jsi)

	# good bye
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
