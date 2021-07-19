from Chrome_quote.locators.quotes_locators import QuotesLocators

""" 
Given one of the specific quote divs, find out the data about the quote( quote content, author, tags )
"""
class QuoteParser:

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'{self.content} by {self.author}'

    @property
    def content(self):
        locator = QuotesLocators.CONTENT
        return self.parent.find_element_by_css_selector(locator).text
    @property
    def author(self):
        locator = QuotesLocators.AUTHOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def tag(self):
        locator = QuotesLocators.TAGS
        return self.parent.find_elements_by_css_selector(locator)


