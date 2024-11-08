class BasePage:
    def __init__(self, browser, chrome=None):
        self.browser = browser
        self.chrome = chrome
    
    def find(self, args):
        return self.browser.find_element(*args)
    
    def finds(self, args):
        return self.browser.find_elements(*args)