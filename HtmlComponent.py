class HtmlComponent:

    def __init__(self, componentType, contents="", classes=[]):
        self.componentType = componentType
        self.contents = contents
        self.classes = classes
        self.indentation = 0

    def render(self):
    	
        if self.contents is None:
            self.contents = ""
        
    	if self.classes is None:
        	self.classes = []

        return "<" + self.componentType + " class=\"" + " ".join(str(x) for x in self.classes) + "\">\n\t" + self.contents + "\n</" + self.componentType + ">\n"


    def setContents(self, contents):
        self.contents = contents

    def setClasses(self, classes):
        self.classes = classes

    def add(self, html_component):
        if self.contents is None:
            self.contents = ""

        html_component.indentation = self.indentation + 1
        self.contents += "\n" + self._properIndent(html_component.render(), self.indentation + 1);

    def _properIndent(self, componentString, indentationLevel):

        individualComponentLines = componentString.split("\n")

        for i in range(1, len(individualComponentLines) - 1):
            individualComponentLines[i] = "\t"*indentationLevel + individualComponentLines[i] 
        
        return "\n".join(str(x) for x in individualComponentLines)
