__author__ = 'Shane'

class CSSFile:

	def __init__(self, src):
		self.src = src
		self.classes = []

	def addClass(self, cssClass):
		self.classes.append(cssClass)

	def render(self):
		fileString = ""

		for each in self.classes:
			fileString += each.render() + "\n"

		return fileString