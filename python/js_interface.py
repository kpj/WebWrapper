import os, os.path
import json

from PyQtX import QtCore, QtWidgets


class JavascriptInterface(QtCore.QObject):
	"""
	@brief Provides sophisticated functions for javascript
	@author kpj
	@version 0.1.0
	"""
	def __init__(self, window, view, args):
		"""Also calls constructor of parent

			@param	window 	Stores access to QMainWindow
			@param	view 	Stores access to QWebView
			@param	args 	Stores access to cmd-line arguments
		"""
		super(JavascriptInterface, self).__init__()

		self.window = window
		self.view = view
		self.args = args

	@QtCore.pyqtSlot(str)
	def log(self, msg):
		"""Easy logging for javascript (prints to terminal)

			@param msg Message to be logged
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
		"""Find root directory of web wrapper

			@retval	Root directory of web wrapper
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

			@retval	content 	Cmd-line arguments passed to python executable
		"""
		return json.dumps(self.args)

	@QtCore.pyqtSlot(str, result=str)
	def read_file(self, fname):
		"""Reads file content

			@param	fname 	Path to file

			@retval result 	Content of file
		"""

		content = open(fname, 'rb').read().decode("utf-8", "replace")
		return content

	@QtCore.pyqtSlot(str, result=str)
	def show_open_file_dialog(self, title):
		"""Asks for file and returns file name

			@param	title	Title of window
		"""
		fname = QtWidgets.QFileDialog.getOpenFileName(None, title, '.')[0]
		return fname

	@QtCore.pyqtSlot(str, result=str)
	def show_open_directory_dialog(self, title):
		"""Asks for dir and returns dir name

			@param	title	Title of window
		"""
		dname = QtWidgets.QFileDialog.getExistingDirectory(None, title, '.')
		return dname

	@QtCore.pyqtSlot(str, result=str)
	def get_directory_content(self, path):
		"""Returns content of given directory

			@param path		Path to directory

			@retval	result	Content of specified directory as dict of the form {"name": {"type": "dir/file"}}
		"""
		path = str(path)
		res = {}
		for c in os.listdir(path):
			res[c] = {'type': 'dir' if os.path.isdir(os.path.join(path, c)) else 'file'}
		return json.dumps(res)

	@QtCore.pyqtSlot(str, str)
	def save_file(self, fname, content):
		"""Saves given content to specified file

			@param	fname 	Path to file
			@param	content Content to be written to file
		"""
		with open(fname, 'w') as fd:
			fd.write(content)

	@QtCore.pyqtSlot(str)
	def create_menu(self, data):
		"""Turns given data structure into menu

			@param data 
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
		self.window.build_menu(json.loads(str(data)))

	@QtCore.pyqtSlot(str, QtCore.QByteArray, result=str)
	def prompt(self, msg, options):
		"""Displays info box in order to choose from given options

			@param	msg		Info message to be displayed
			@param	options	Options to choose from

			@retval	result 	Chosen option
		"""

		w = QtWidgets.QDialog()
		w.exec_()

		return "hi"

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
			getattr(obj, str(func_name))(*args)
		else:
			print('> Invalid target')
