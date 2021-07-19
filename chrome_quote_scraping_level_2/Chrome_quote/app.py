from selenium import webdriver

from pages.quotes_pages import QuotesPage
chrome = webdriver.Chrome(executable_path = 'J:\chromedriver_win32_unzip\chromedriver_win32\chromedriver.exe')
chrome.get("https://quotes.toscrape.com")
page = QuotesPage(chrome)


for quote in page.quotes:
    print(quote)

