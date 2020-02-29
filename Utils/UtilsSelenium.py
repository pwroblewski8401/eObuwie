class UtilsSelenium:
    def __init__(self, _driver):
        self.driver = _driver

    def get_webpage_title(self):
        return self.driver.title