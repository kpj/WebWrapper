import json, os
from PyQtX import QtWebKitWidgets, QtCore, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, view):
		super(MainWindow, self).__init__()

		self.installEventFilter(self)

		self.view = view
		self.setCentralWidget(view)

	def eventFilter(self, object, event):
		if event.type() == QtCore.QEvent.WindowActivate:
			self.view.evtHandler("focusin", [])
		elif event.type() == QtCore.QEvent.WindowDeactivate:
			self.view.evtHandler("focusout", [])

		return False

	def gen_event_handler(self, event):
		def func():
			self.view.evtHandler(event, [])
		return func

	def build_menu(self, data):
		self.statusBar()
		menubar = self.menuBar()

		for menu_d in data:
			menu = menubar.addMenu(menu_d['name'])

			for entry in menu_d['items']:
				tmp = QtWidgets.QAction(entry['name'], self)
				tmp.setShortcut(entry['shortcut'])
				tmp.setStatusTip(entry['statustip'])
				tmp.triggered.connect(
					self.gen_event_handler(entry['trigger'])
				)

				menu.addAction(tmp)

class Viewer(QtWebKitWidgets.QWebView):
	def __init__(self, args):
		QtWebKitWidgets.QWebView.__init__(self)

		self.page().mainFrame().loadFinished.connect(self.loadFinished)
		self.page().mainFrame().javaScriptWindowObjectCleared.connect(
			self.javaScriptWindowObjectCleared
		)

		self.load(QtCore.QUrl('file:///' + os.path.abspath(args['file'])))

	def evtHandler(self, key, args):
		args = json.dumps(args)
		key = json.dumps(key)

		print("Events.__pyTrigger("+key+", "+args+")")
		self.page().mainFrame().evaluateJavaScript(
			"Events.__pyTrigger("+key+", "+args+")"
		)

	def keyPressEvent(self, e):
		self.evtHandler("keypress", [str(e.key())])

		QtWebKitWidgets.QWebView.keyPressEvent(self, e)

	def keyReleaseEvent(self, e):
		self.evtHandler("keyrelease", [str(e.key())])

		QtWebKitWidgets.QWebView.keyReleaseEvent(self, e)

	def loadFinished(self, ok):
		self.show()

	def set_js_interface(self, jsi):
		self.js_interface = jsi

	def javaScriptWindowObjectCleared(self):
		self.page().mainFrame().addToJavaScriptWindowObject(
			"PyInterface",
			self.js_interface
		)
