import os, os.path
import json
from PyQt4 import QtCore, QtGui


class JavascriptInterface(QtCore.QObject):
	"""Provides e.g. fs-access in javascript itself
	"""
	@QtCore.pyqtSlot(str)
	def log(self, msg):
		"""Easy logging for javascript (prints to terminal)
		"""
		print(msg)

	@QtCore.pyqtSlot(str, result=str)
	def read_file(self, fname):
		"""Reads file content
		"""

		return open(fname, 'r').read()

	@QtCore.pyqtSlot(str, result=str)
	def show_open_file_dialog(self, title):
		"""Asks for file and returns file name
		"""
		fname = QtGui.QFileDialog.getOpenFileName(None, title, '.')
		return fname

	@QtCore.pyqtSlot(str, result=str)
	def show_open_directory_dialog(self, title):
		"""Asks for dir and returns dir name
		"""
		dname = QtGui.QFileDialog.getExistingDirectory(None, title, '.')
		return dname

	@QtCore.pyqtSlot(str, result=str)
	def get_directory_content(self, path):
		"""Returns content of given directory
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