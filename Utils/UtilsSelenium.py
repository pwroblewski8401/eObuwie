from datetime import datetime
import os

class UtilsSelenium:
    def __init__(self, _driver):
        self.driver = _driver

    def get_webpage_title(self):
        return self.driver.title

    def make_screenshot(self, test_name):
        if(os.path.isdir(f'{os.getcwd()}/Artifacts/Screens/')):
            pass
            #TOLOG: dir exist
        else:
            os.mkdir(f'{os.getcwd()}/Artifacts/Screens/')


        name = str.replace(test_name, ".", "_")
        dir = 'Artifacts/Screens/'
        sceenshotFileName = f'{name}_{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.png'
        print(f'{dir}{sceenshotFileName}')
        self.driver.save_screenshot(f'{dir}{sceenshotFileName}')

