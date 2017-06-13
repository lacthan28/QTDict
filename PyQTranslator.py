# -*- coding: utf-8 -*-

from tkinter import *

from qtdict.GUI.menubarGUI import *


class PyQTranslator(Tk):
	def __init__(self):
		super().__init__()
		self.title('Py Quick Translator')
		self.geometry("500x250+300+300")

	def main(self):
		app = Frame(self)
		menu = menubarGUI(self)
		self.config(menu = menu)
		self.mainloop()


run = PyQTranslator()
run.main()
