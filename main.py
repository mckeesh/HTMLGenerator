from HtmlComponent import HtmlComponent
from HtmlSource import HtmlSource

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

	print html.render()

main()