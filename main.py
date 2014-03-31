import sys
from PyQt5 import QtWidgets

import python.gui, python.js_interface


def main():
	if len(sys.argv) != 2:
		print('Usage: %s <index.html>' % sys.argv[0])
		sys.exit(1)

	app = QtWidgets.QApplication(sys.argv)

	# create main window
	view = python.gui.Viewer(sys.argv[1])
	window = python.gui.MainWindow(view)

	# create js interface
	jsi = python.js_interface.JavascriptInterface(window, view)
	view.set_js_interface(jsi)

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
