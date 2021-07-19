from Chrome_quote.locators.quotes_page_locators import QuotesPageLocators
from Chrome_quote.parsers.quotes import QuoteParser
class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE
        quote_tag = self.browser.find_elements_by_css_selector(locator)
        #print(quote_tag)
        return [QuoteParser(e) for e in quote_tag]
