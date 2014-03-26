import json
from PyQt5 import QtWebKitWidgets, QtCore, QtGui, QtWidgets

import python.js_interface


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, view):
		super(MainWindow, self).__init__()

		self.installEventFilter(self)

		self.view = view

		self.setCentralWidget(view)
		self.initUI()

	def eventFilter(self, object, event):
		if event.type() == QtCore.QEvent.WindowActivate:
			self.view.evtHandler("focusin", [])
		elif event.type() == QtCore.QEvent.WindowDeactivate:
			self.view.evtHandler("focusout", [])

		return False

	def initUI(self):
		# TODO: move this to javascript

		self.statusBar()

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		for a in self.getFileMenu():
			fileMenu.addAction(a)
		
		getattr(self, 'setWindowTitle')('WebWrapper')    
		getattr(self, 'show')()

	def getFileMenu(self):
		actions = []

		#openFileAction = QtGui.QAction('&Open File', self)        
		#openFileAction.setShortcut('Ctrl+O')
		#openFileAction.setStatusTip('Open new file')
		#openFileAction.triggered.connect(self.openFileAction)
		#actions.append(openFileAction)

		return actions

class Viewer(QtWebKitWidgets.QWebView):
	def __init__(self):
		QtWebKitWidgets.QWebView.__init__(self)

		self.page().mainFrame().loadFinished.connect(self.loadFinished)
		self.page().mainFrame().javaScriptWindowObjectCleared.connect(
			self.javaScriptWindowObjectCleared
		)

		self.load(QtCore.QUrl('./view/index.html'))

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

	def javaScriptWindowObjectCleared(self):
		print("Javascript object added")
		self.page().mainFrame().addToJavaScriptWindowObject(
			"PyInterface",
			python.js_interface.JavascriptInterface(self)
		)
