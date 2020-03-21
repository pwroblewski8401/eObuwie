from datetime import datetime
import os

class UtilsSelenium:
    def __init__(self, _driver, logger):
        self.logger = logger
        self.driver = _driver

    def get_webpage_title(self):
        return self.driver.title

    def take_screenshot(self, test_name):
        dirArtifact = f'{os.getcwd()}\\Artifacts\\'
        if not os.path.isdir(dirArtifact):
            os.mkdir(dirArtifact)
        dir = f'{os.getcwd()}\\Artifacts\\Screens\\'
        if(os.path.isdir(dir)):
            pass
            #TOLOG: dir exist
        else:
            os.mkdir(dir)

        name = str.replace(test_name, ".", "_")
        sceenshotFileName = f'{name}_{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.png'
        print(f'{dir}{sceenshotFileName}')
        self.driver.save_screenshot(f'{dir}{sceenshotFileName}')
        self.logger.info(f"Taking screenshot! File: {dir}{sceenshotFileName}")


