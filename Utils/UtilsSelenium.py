from datetime import datetime
import os


class UtilsSelenium:
    def __init__(self, _driver, logger):
        self.logger = logger
        self.driver = _driver

    def get_webpage_title(self):
        return self.driver.title

    def takeScreenshot(self, test_name):
        dir_artifact = f'{os.getcwd()}\\Artifacts\\'
        if not os.path.isdir(dir_artifact):
            os.mkdir(dir_artifact)
        dir = f'{os.getcwd()}\\Artifacts\\Screens\\'
        if os.path.isdir(dir):
            pass
            #TOLOG: dir exist
        else:
            os.mkdir(dir)

        name = str.replace(test_name, ".", "_")
        sceenshot_file_name = f'{name}_{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.png'
        print(f'{dir}{sceenshot_file_name}')
        self.driver.save_screenshot(f'{dir}{sceenshot_file_name}')
        self.logger.info(f"Taking screenshot! File: {dir}{sceenshot_file_name}")


