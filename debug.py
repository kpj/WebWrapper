import sys
from PyQt5 import QtCore, QtWidgets, QtWebKitWidgets


html = """
<html>
	<head>
	</head>
	<body>
		Hello World!

		<script>
			window.onload = function() {
				alert(PyInterface);
				PyInterface.print_msg("It works!");
			}
		</script>
	</body>
</html>
"""

class Test(QtCore.QObject):
	@QtCore.pyqtSlot(str)
	def print_msg(self, msg):
		print(msg)

class Viewer(QtWebKitWidgets.QWebView):
	def __init__(self):
		QtWebKitWidgets.QWebView.__init__(self)

		self.page().mainFrame().loadFinished.connect(self.loadFinished)
		self.page().mainFrame().javaScriptWindowObjectCleared.connect(
			self.javaScriptWindowObjectCleared
		)

		self.setHtml(html)

	def loadFinished(self, ok):
		print('done', ok)

	def javaScriptWindowObjectCleared(self):
		print("Javascript object added")
		self.page().mainFrame().addToJavaScriptWindowObject(
			"PyInterface",
			Test()
		)

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, view):
		super(MainWindow, self).__init__()

		self.setCentralWidget(view)
		self.show()

def main():
	app = QtWidgets.QApplication(sys.argv)

	# create main window
	view = Viewer()
	main_window = MainWindow(view)

	sys.exit(app.exec_())

if __name__ == '__main__':
	main()