import logging

class HtmlSource:

    def __init__(self, src, manualDependecy=""):
        self._src = src
        self.indentation = 0
        self.fileExtension = src.split(".")[-1]
        self.manualDependency = manualDependecy
        self.hasRendered = False

    def setSource(self, src):
        self._src = src
        self.hasRendered = False

    def render(self):

        self.hasRendered = True

        if self.manualDependency == "":

            if self.fileExtension == "css":
                return "rel=\"stylesheet\" type=\"text/css\" href=\"" + self._src + "\">"
            elif self.fileExtension == "js":
                return "<script src=\"" + self._src + "\"></script>"
            else:
                self.hasRendered = False
                raise Exception("This generator is still quite stupid and doesn't know about the " + self.fileExtension + ". "
                                "Feel free to add your own syntax to the code for your own "
                                "type of dependency.\nIf you just want to add a dependency the quick and dirty way, add it to "
                                "manualDependency like this:\nweirdDependency = HtmlDependency(None, '<script src=\"file.js\"></script>')\n"
                                "Then call dependency.render()")
        else:
            return self.manualDependency

