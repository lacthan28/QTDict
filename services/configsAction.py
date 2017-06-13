# -*- coding: utf-8 -*-
import configparser


def getFilePath():
	import os
	relative_path = 'pyqtranslator/configs.ini'
	current_dir = os.getcwd()
	return os.path.join(current_dir, relative_path)


class configsAction:
	def __init__(self, master, parent, value):
		self.master = master
		self.parent = parent
		self.isFullscreenChecked = value
		self.isFullscreen = False
		self.config = configparser.ConfigParser()
		self.createConfigFile()

	def createConfigFile(self):
		self.config.add_section('THEME')
		self.config.set('THEME', 'FullscreenMode', 'False')
		try:
			with open(getFilePath(), 'w') as file:
				self.config.write(file)
		except:
			print(getFilePath())

	def fullscreenChecked(self):
		"""
		Check checkbutton fullscreen is checked or not and change the display mode
		:return:
		"""
		self.selection = self.isFullscreenChecked.get()
		if self.selection == 1:
			self.config['THEME']['FullscreenMode'] = 'True'
		elif self.selection == 0:
			self.config['THEME']['FullscreenMode'] = 'False'

	def onOk(self):
		try:
			with open(getFilePath(), 'r') as file:
				self.config.read(file)
				theme = self.config['THEME']
				self.isFullscreen = theme['FullscreenMode']
				self.master.attributes('-fullscreen', self.isFullscreen)
		except:
			print(getFilePath())

	def onCancel(self):
		self.parent.destroy()
