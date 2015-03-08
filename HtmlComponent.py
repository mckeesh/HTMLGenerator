import logging
from HtmlSource import HtmlSource

class HtmlComponent:

    def __init__(self, componentType, contents="", classes=[]):
        self.componentType = componentType
        self.contents = contents
        self.classes = classes
        self.indentation = 0
        self.subelements = []
        self.hasRendered = False

        if componentType is "html":
            self.head = HtmlComponent("head")
            self.add(self.head)

    def render(self):
        if self.contents is None:
            self.contents = ""

        for subelement in self.subelements:
            self.contents += "\n" + self._properIndent(subelement.render(), self.indentation)

        classPortion = ""
        if self.classes is None:
            self.classes = []
        elif not self.classes == []:
            classPortion = " class=\"" + " ".join(str(x) for x in self.classes) + "\""

        self.hasRendered = True

        for i in range(len(self.subelements)):
            self.subelements[i].render()

        componentBody = ""
        if not self.contents == "":
            componentBody = "\n\t" + self.contents + "\n"

        return "<" + self.componentType + classPortion + ">" + componentBody + "</" + self.componentType + ">\n"

    def appendToContents(self, contents):
        if self.contents is None:
            self.contents = ""

        self.contents += contents
        self.hasRendered = False

    def clearContents(self):
        self.contents = ""
        self.hasRendered = False

    def setClasses(self, classes):
        self.classes = classes
        self.hasRendered = False

    def add(self, html_component):
        if self.contents is None:
            self.contents = ""

        if self.hasRendered:
            logging.warning("Parent component has already been rendered, so added component will not be visible.")

        html_component.indentation = self.indentation + 1
        self.subelements.append(html_component)

        self.hasRendered = False

    def addSource(self, filelink):
        dependency = HtmlSource(filelink)
        self.head.appendToContents(dependency.render())
        self.hasRendered = False

    def addManualSource(self, manualLine):
        dependency = HtmlSource(None, manualLine)
        self.head.add(dependency)
        self.hasRendered = False

    def _properIndent(self, componentString, indentationLevel):

        individualComponentLines = componentString.split("\n")

        tabs = "\t"*indentationLevel

        for i in range(len(individualComponentLines) - 1):
            individualComponentLines[i] = tabs + individualComponentLines[i]
        
        return "\n".join(str(x) for x in individualComponentLines)
