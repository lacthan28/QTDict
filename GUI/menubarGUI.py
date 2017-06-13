# -*- coding: utf-8 -*-
from ..services.menubarAction import *


class menubarGUI(Menu):
	def __init__(self, parent):
		Menu.__init__(self, parent)
		self.parent = parent
		self.mnuAction = menubarAction(parent)
		self.createMenuFile()
		self.createmenuConfigs()

	def createMenuFile(self):
		self.mnuFile = Menu(self, tearoff = 0)

		self.mnuFile.add_command(label = "New Window", accelerator = "Ctrl+N", command = self.mnuAction.menuNewWindow)
		self.mnuFile.add_separator()

		self.mnuFile.add_command(label = "Open", accelerator = "Ctrl+O", command = self.mnuAction.menuOpen)
		self.mnuFile.add_command(label = "Save", accelerator = "Ctrl+S", command = self.mnuAction.menuSave)
		self.mnuFile.add_command(label = "Export To Word", command = self.mnuAction.menuExportToWord)
		self.mnuFile.add_separator()

		self.mnuFile.add_command(label = "Exit", accelerator = "Alt+F4", command = self.mnuAction.menuExit)

		# self.parent.bind('<Control-o>', self.mnuAction.menuOpen())

		self.add_cascade(label = 'File', menu = self.mnuFile)

	def createmenuConfigs(self):
		self.mnuConfigs = Menubutton(self, text = 'Configs')
		self.add_command(label = 'Configs', command = self.mnuAction.mnuConfigs)
