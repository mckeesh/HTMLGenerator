from HtmlComponent import HtmlComponent

def main():
	html = HtmlComponent("html", None, ["class1", "class2", "class3"])

	mainContainer = HtmlComponent("div", "Hi!", ["mainCss"])

	smallerDiv = HtmlComponent("div", "Hi again!", ["smallerCss", "blue"])

	mainContainer.add(smallerDiv)

	html.add(mainContainer)

	print html.render()

main()