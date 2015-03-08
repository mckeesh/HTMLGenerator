__author__ = 'Shane'

class CSSClass:

	def __init__(self, name, selector="."):
		self.name = name
		self.selector = selector
		self.attributes = {}
		self.comments = []

	def addAttribute(self, key, value):
		self.attributes[key] = value

	def addComment(self, comment):
		self.comments.append(str(comment))

	def render(self):

		renderedClass = ""

		if not self.name[0] == ".":
			self.name = self.selector + self.name

		for comment in self.comments:
			renderedClass += "/* " + str(comment) + "*/\n"

		renderedClass += self.name + " {\n"
		for each in self.attributes:
			renderedClass += "\t" + each + " : "

			value = self.attributes[each]
			if isinstance(value, list):
				valsSeparatedBySpaces = " ".join(str(each) for each in value) + ";\n"
				renderedClass += valsSeparatedBySpaces
			else:
				renderedClass += str(self.attributes[each]) + ";\n"

		renderedClass += "}\n"

		return renderedClass