import os, os.path
import json

from PyQt5 import QtCore, QtWidgets


class JavascriptInterface(QtCore.QObject):
	"""
	@brief Provides sophisticated functions for javascript
	@author kpj
	@version 0.1
	"""
	def __init__(self, window, view, args):
		super(JavascriptInterface, self).__init__()

		self.window = window
		self.view = view
		self.args = args

	@QtCore.pyqtSlot(str)
	def log(self, msg):
		"""Easy logging for javascript (prints to terminal)
		"""
		print(msg)

	@QtCore.pyqtSlot()
	def shutdown(self):
		"""Quits Qt application
		"""
		app = QtWidgets.QApplication.instance()
		app.closeAllWindows()

	@QtCore.pyqtSlot(result=str)
	def get_root_dir(self):
		"""Returns root directory of web wrapper
		"""
		return os.path.abspath(
			os.path.join(
				os.path.dirname(
					os.path.realpath(__file__)
				), '..'
			)
		)

	@QtCore.pyqtSlot(result=str)
	def get_args(self):
		"""Returns cmd-line arguments provided to python
		"""
		return json.dumps(self.args)

	@QtCore.pyqtSlot(str, result=str)
	def read_file(self, fname):
		"""Reads file content
		"""

		return open(fname, 'r').read()

	@QtCore.pyqtSlot(str, result=str)
	def show_open_file_dialog(self, title):
		"""Asks for file and returns file name
		"""
		fname = QtWidgets.QFileDialog.getOpenFileName(None, title, '.')[0]
		return fname

	@QtCore.pyqtSlot(str, result=str)
	def show_open_directory_dialog(self, title):
		"""Asks for dir and returns dir name
		"""
		dname = QtWidgets.QFileDialog.getExistingDirectory(None, title, '.')
		return dname

	@QtCore.pyqtSlot(str, result=str)
	def get_directory_content(self, path):
		"""Returns content of given directory

			@param path		Path to directory

			@retval			Content of specified directory as dict of the form {"name": {"type": "dir/file"}}
		"""
		res = {}
		for c in os.listdir(path):
			res[c] = {'type': 'dir' if os.path.isdir(c) else 'file'}
		return json.dumps(res)

	@QtCore.pyqtSlot(str, str)
	def save_file(self, fname, content):
		"""Saves given content to specified file
		"""
		with open(fname, 'w') as fd:
			fd.write(content)

	@QtCore.pyqtSlot(str)
	def create_menu(self, data):
		"""Turns given data structure into menu
		   structure:
		    [
		   		{
		   			"name": "foo",
		   			"items": [
		   				{
		   					"name": "bar",
		   					"shortcut": "Ctrl+O",
		   					"statustip": "baz",
		   					"trigger": "func_name"
		   				}
		   			]
		   		}
		   	]
		"""
		self.window.build_menu(json.loads(data))

	@QtCore.pyqtSlot(str, str, QtCore.QByteArray)
	def execute(self, target, func_name, args):
		"""Call function on QMainWindow and QWebView from within javascript
		
			@param	target		'window' for QMainWindow, 'view' for QWebView
			@param	func_name	Name of function to be called
			@param	args		List of arguments given to specified function
		"""
		args = [e.data().decode('utf-8') for e in args.split(',') if len(e) > 0]

		obj = None
		if target == 'window':
			obj = self.window
		elif target == 'view':
			obj = self.view

		print('Calling "' + func_name + '" with "' + str(args) + '" on "' + target + '"')
		
		if obj:
			getattr(obj, func_name)(*args)
		else:
			print('> Invalid target')
