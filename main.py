from HtmlComponent import HtmlComponent
from HtmlSource import HtmlSource
from CSSClass import CSSClass
from CSSFile import CSSFile

def main():
	html = HtmlComponent("html", None, ["class1", "class2", "class3"])
	html.addSource("javascript.js")
	mainContainer = HtmlComponent("div", "Hi!", ["mainCss"])
	smallerDiv = HtmlComponent("div", "Hi again!", ["smallerCss", "blue"])
	smallestDiv = HtmlComponent("div", "boo")
	smallerDiv.add(smallestDiv)
	mainContainer.add(smallerDiv)
	html.add(mainContainer)
	html.appendToContents("top level")

	# print html.render()

	classy = CSSClass("testClass", "#")
	classy.addAttribute("color", "black")
	classy.addAttribute("font-size", 24)
	classy.addAttribute("border", ["1px", "black", "solid"])
	# print classy.render()

	classy2 = CSSClass("testClass2", ".")
	classy2.addAttribute("color", "blue")
	classy2.addAttribute("font-size", 24)
	classy2.addAttribute("border", ["1px", "black", "solid"])
	classy2.addComment("Here's my awesome comment")

	cssFile = CSSFile("testFile")
	cssFile.addClass(classy)
	cssFile.addClass(classy2)
	print cssFile.render()


main()