# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import *

from ..services.configsAction import *


class Configs(Toplevel):
	"""
	This class is use for setting application
	"""

	def __init__(self, parent):
		Toplevel.__init__(self, parent)
		self.parent = parent
		self.title('Configs')
		self.value = IntVar()
		self.configsAction = configsAction(parent, self, self.value)
		self.initUI()

	def initUI(self):
		"""
		Create GUI Widget
		:return:
		"""

		self.lblSettings = Label(self, text = '-*- Settings -*-')
		self.chkFullscreen = Checkbutton(self, text = 'Fullscreen', variable = self.value, onvalue = 1, offvalue = 0,
		                                 command = self.configsAction.fullscreenChecked)
		self.btnOk = Button(self, text = 'Ok', command = self.configsAction.onOk)
		self.btnCancel = Button(self, text = 'Cancel', command = self.configsAction.onCancel)

		self.lblSettings.grid(column = 0, row = 0)
		self.chkFullscreen.grid(column = 0, row = 1)
		self.btnOk.grid(column = 0, row = 2)
		self.btnCancel.grid(column = 1, row = 2)
