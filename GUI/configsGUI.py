# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import *
from ..services.configsAction import configsAction


class MainConfig(Tk):
	def __init__(self, parent):
		super().__init__()
		self.parent = parent
		self.initUI()

	def initUI(self):
		self.notebook = Notebook(self)
		self.tab1 = FullscreenConfigs(self.parent, self)
		self.tab2 = LanguageConfigs(self)

		self.notebook.add(self.tab1, text = "Fullscreen")
		self.notebook.add(self.tab2, text = 'Language')
		self.notebook.pack(expand = 1, fill = BOTH)

		self.mainloop()


class LanguageConfigs(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent

		self.configsAction = configsAction(parent, parent, self)
		self.btnApply = Button(self, text = 'Apply', command = self.configsAction.onApply)
		self.btnCancel = Button(self, text = 'Cancel', command = self.configsAction.onCancel)
		self.btnCancel.grid(column = 1, row = 0)
		self.btnApply.grid(column = 0, row = 0)


class FullscreenConfigs(Frame):
	"""
	This class is use for setting application
	"""

	def __init__(self, master, parent):
		Frame.__init__(self, parent)
		self.parent = parent
		self.master = master
		self.value = IntVar(value = 0)
		self.configsAction = configsAction(master, parent, self, self.value)
		self.initUI()

	def initUI(self):
		"""
		Create GUI Widget
		:return:
		"""

		self.lblSettings = Label(self, text = '-*- Fullscreen -*-')
		self.chkFullscreen = Checkbutton(self, text = 'Enable', variable = self.value, onvalue = 1, offvalue = 0,
		                                 command = self.configsAction.fullscreenChecked)
		self.btnApply = Button(self, text = 'Apply', command = self.configsAction.onApply)
		self.btnCancel = Button(self, text = 'Cancel', command = self.configsAction.onCancel)

		self.lblSettings.grid(column = 0, row = 0)
		self.chkFullscreen.grid(column = 0, row = 1)
		self.btnCancel.grid(column = 1, row = 2)
		self.btnApply.grid(column = 0, row = 2)
