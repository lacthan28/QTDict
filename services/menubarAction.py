# -*- coding: utf-8 -*-
from tkinter import filedialog

from ..GUI.configsGUI import *


class menubarAction:
	def __init__(self, parent):
		self.parent = parent

	# -----------------------------------------
	# Menu File
	# -----------------------------------------

	def menuNewWindow(self):
		pass

	def menuOpen(self):
		self.name = filedialog.askopenfilename(filetypes = (("Text File", "*.txt"), ("All Files", "*.*")),
		                                       title = 'Open file...')
		try:
			with open(self.name, 'r') as fileOpen:
				print(fileOpen.read())
		except:
			print("File not found!")

	def menuSave(self):
		self.file = filedialog.asksaveasfile(mode = "w", defaultextension = ".txt",
		                                     filetypes = (("Text File", "*.txt"), ("All Files", "*.*")))
		if self.file is None:
			return
		text2save = "language=vi\nlocale=vn"
		self.file.write(text2save)
		self.file.close()

	def menuExportToWord(self):
		pass

	def menuExit(self):
		self.parent.quit()

	# -----------------------------------------
	# Menu Configs
	# -----------------------------------------

	def mnuConfigs(self):
		Configs(self.parent)